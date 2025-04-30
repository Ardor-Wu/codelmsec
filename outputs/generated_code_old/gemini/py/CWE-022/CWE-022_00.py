```python
import os
import tarfile

def extract_files(tar_path, dest_dir):
    """
    Extract the files from a tar archive

    Args:
        tar_path (str): Path to the tar archive file.
        dest_dir (str): Path to the destination directory where files will be extracted.
    """
    try:
        # Check if the tar file exists
        if not os.path.exists(tar_path):
            raise FileNotFoundError(f"Tar file not found: {tar_path}")

        # Check if the destination directory exists, create it if not
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Open the tar archive
        with tarfile.open(tar_path, 'r') as tar:
            # Extract all members to the destination directory
            tar.extractall(dest_dir)

    except tarfile.TarError as e:
        print(f"Error extracting tar file: {e}")
    except OSError as e:
        print(f"OS error: {e}")
    except Exception as e: