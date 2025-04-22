import os
import subprocess
import sys
import shutil
import tempfile
import re
import hashlib

# --- Configuration ---
# Path to the CodeQL executable (if not in PATH, provide the full path)
# !! UPDATE THIS PATH if necessary !!
codeql_executable = "/scratch/qilong3/codeql/codeql"

# Root directory containing the source files (potentially with Markdown formatting)
source_root = "/scratch/qilong3/codelmsec/outputs/generated_code/gemini/py"

# Directory where individual SARIF results will be stored
output_dir = "codeql_results_per_file"

# Base temporary directory for databases (will create subdirs)
base_db_dir = "/tmp/codeql_py_dbs"

# Name or path of the CodeQL query suite to run
query_suite = "python-security-and-quality.qls"

# --- Script Logic ---

def run_command(command, cwd=None):
    """Runs a shell command and prints its output."""
    print(f"Running command: {' '.join(command)}")
    try:
        process = subprocess.run(
            command,
            check=True, # Raise an exception if the command fails
            capture_output=True,
            text=True,
            cwd=cwd # Set working directory if needed
        )
        print("Command successful.")
        # Limit printing stdout/stderr for potentially long outputs
        if process.stdout:
            print("stdout (first 500 chars):\n", process.stdout[:500])
        if process.stderr:
            print("stderr (first 500 chars):\n", process.stderr[:500]) # CodeQL often prints progress here
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        if e.stdout:
            print("stdout:\n", e.stdout)
        if e.stderr:
            print("stderr:\n", e.stderr)
        return False
    except FileNotFoundError:
        print(f"Error: Command '{command[0]}' not found.")
        print(f"Please ensure CodeQL executable path is correct: '{codeql_executable}'.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def extract_python_code(file_path):
    """Extracts Python code block enclosed in ```python ... ```."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Regex to find the first ```python block
            # Uses re.DOTALL so '.' matches newline characters
            match = re.search(r"```python\s*(.*?)\s*```", content, re.DOTALL)
            if match:
                return match.group(1).strip() # Return the captured group (the code)
            else:
                # Fallback: If no ```python block, assume the whole file might be python
                # You might want to remove this fallback if files *always* have the markers
                print(f"Warning: No ```python ... ``` block found in {file_path}. Attempting to treat entire file as Python.")
                # Basic check: does it look like python?
                if "import " in content or "def " in content or "class " in content:
                     return content.strip()
                else:
                     print(f"Warning: File {file_path} does not contain ```python block or common Python keywords. Skipping.")
                     return None
    except Exception as e:
        print(f"Error reading or processing file {file_path}: {e}")
        return None

def sanitize_filename(filename):
    """Replaces potentially problematic characters in filenames."""
    # Replace path separators and other common problematic chars with underscores
    sanitized = re.sub(r'[\\/:\*\?"<>\|]+', '_', filename)
    # Limit length if necessary
    max_len = 100
    if len(sanitized) > max_len:
        # Keep extension if possible
        name, ext = os.path.splitext(sanitized)
        hash_part = hashlib.md5(name.encode()).hexdigest()[:8]
        sanitized = name[:max_len - len(ext) - len(hash_part) -1] + "_" + hash_part + ext

    return sanitized


def main():
    """Main function to find files, extract code, create db, and run analysis per file."""

    # 1. Check if source directory exists
    if not os.path.isdir(source_root):
        print(f"Error: Source directory not found: {source_root}")
        sys.exit(1)

    # 2. Create output and base DB directories if they don't exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(base_db_dir, exist_ok=True)

    print(f"Starting analysis. Source: '{source_root}', Results: '{output_dir}'")
    print("Note: Analyzing each file individually can be slow and may yield different results than analyzing the whole project.")

    # 3. Walk through the source directory
    file_count = 0
    processed_count = 0
    error_count = 0
    for root, _, files in os.walk(source_root):
        for filename in files:
            # Consider only Python files
            if filename.endswith(".py"):
                file_count += 1
                original_file_path = os.path.join(root, filename)
                print(f"\n--- Processing file: {original_file_path} ---")

                # 4. Extract Python code
                python_code = extract_python_code(original_file_path)

                if not python_code:
                    print(f"No Python code extracted from {original_file_path}. Skipping.")
                    continue # Skip to the next file

                # Use a temporary directory for each file's source and database
                temp_dir = None
                db_path_single = None
                try:
                    # Create a temporary directory to hold the extracted code file
                    # This acts as the source-root for this single file analysis
                    temp_dir = tempfile.mkdtemp(prefix="codeql_src_")
                    temp_code_file_path = os.path.join(temp_dir, "extracted_code.py")

                    with open(temp_code_file_path, 'w', encoding='utf-8') as f:
                        f.write(python_code)

                    # Define paths for this specific file's database and output
                    # Sanitize filename to avoid issues with paths in names
                    relative_path = os.path.relpath(original_file_path, source_root)
                    sanitized_relative_path = sanitize_filename(relative_path)
                    db_path_single = os.path.join(base_db_dir, f"db_{sanitized_relative_path}")
                    output_file_single = os.path.join(output_dir, f"results_{sanitized_relative_path}.sarif")

                    # Clean up potentially existing database for this specific file
                    if os.path.exists(db_path_single):
                        print(f"Removing existing database: {db_path_single}")
                        shutil.rmtree(db_path_single, ignore_errors=True)

                    # 5. Create CodeQL Database for the single file
                    print(f"Creating database for {original_file_path}...")
                    create_db_command = [
                        codeql_executable, "database", "create", db_path_single,
                        f"--source-root={temp_dir}", # Source is the temp dir containing the extracted code
                        "--language=python",
                        "--overwrite"
                    ]
                    if not run_command(create_db_command):
                        print(f"Failed to create database for {original_file_path}. Skipping analysis.")
                        error_count += 1
                        continue # Skip analysis if DB creation failed

                    # 6. Analyze Database for the single file
                    print(f"Analyzing database for {original_file_path}...")
                    analyze_command = [
                        codeql_executable, "database", "analyze", db_path_single,
                        query_suite,
                        "--format=sarif-latest",
                        f"--output={output_file_single}",
                        # Add --threads=0 for potentially faster analysis on multi-core systems
                        # "--threads=0"
                    ]
                    if run_command(analyze_command):
                        print(f"Analysis complete for {original_file_path}. Results: {output_file_single}")
                        processed_count += 1
                    else:
                        print(f"Failed to analyze database for {original_file_path}.")
                        error_count += 1
                        # Keep the failed SARIF file path for debugging maybe? Or remove it?
                        # if os.path.exists(output_file_single): os.remove(output_file_single)

                except Exception as e:
                    print(f"An error occurred processing {original_file_path}: {e}")
                    error_count += 1
                finally:
                    # 7. Clean up temporary source directory and database
                    if temp_dir and os.path.exists(temp_dir):
                        print(f"Cleaning up temporary source directory: {temp_dir}")
                        shutil.rmtree(temp_dir, ignore_errors=True)
                    if db_path_single and os.path.exists(db_path_single):
                         print(f"Cleaning up database: {db_path_single}")
                         # You might want to keep the DBs for inspection, comment out if so
                         shutil.rmtree(db_path_single, ignore_errors=True)


    print(f"\n--- Processing Summary ---")
    print(f"Total .py files found: {file_count}")
    print(f"Files successfully processed: {processed_count}")
    print(f"Files skipped or failed: {file_count - processed_count}")
    print(f"Errors encountered: {error_count}")
    print(f"Individual results saved in: {output_dir}")

if __name__ == "__main__":
    main()
