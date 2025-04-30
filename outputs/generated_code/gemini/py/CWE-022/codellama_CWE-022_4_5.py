```python
import os
import tarfile



def main():
    # Create a list to store tar file names
    tars = []

    # Check the current directory for files with a.gz extension
    for filename in os.listdir("."):
        if filename.endswith(".tar.gz"):
            tars.append(filename)

    # Iterate through the tar files
    for tar_filename in tars:
        try:
            # Open the tar file
            with tarfile.open(tar_filename, "r:gz") as tar:
                # Extract all members to a directory named after the tar file (without extension)
                extract_dir = tar_filename[:-7]  # Remove .tar.gz
                os.makedirs(extract_dir, exist_ok=True)  # Create directory if it doesn't exist
                tar.extractall(extract_dir)
                print(f"Extracted {tar_filename} to {extract_dir}")

        except tarfile.TarError as e:
            print(f"Error extracting {tar_filename}: {e}")
        except Exception as e:  # Catch other potential errors (e.g., permission issues)
            print(f"An unexpected error occurred while processing {tar_filename}: {e}")


if __name__ == "__main__":
    main()

```