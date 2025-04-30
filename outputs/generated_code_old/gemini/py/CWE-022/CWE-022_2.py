```python
import tarfile

def extract_tar(tar_path, dest_dir):
    """
    Extract all files from a tar archive to a specified directory.
    """
    try:
        # Open the tar archive in read mode
        with tarfile.open(tar_path, 'r') as tar:
            # Extract all members to the destination directory
            tar.extractall(path=dest_dir)
    except tarfile.TarError as e:
        # Handle tar-related errors
        print(f"Error extracting tar archive: {e}")
    except Exception as e:
        # Handle other potential errors
        print(f"An unexpected error occurred: {e}")



```

```python
import tarfile
import os

def extract_archive(file_name):
    '''
    Extract all files from a tar archive to the current working directory.
    '''
    try:
        # Open the tar archive
        with tarfile.open(file_name, 'r') as tar:
            # Extract all members to the current directory
            tar.extractall()
    except tarfile.TarError as e:
        # Handle tar-related errors
        print(f"Error extracting tar archive: {e}")
    except Exception as e:
        # Handle other potential errors
        print(f"An unexpected error occurred: {e}")

```

```python
import tarfile
import os

def extract_and_delete_image(image_path):
    ''' 
    Extract a tar.gz image archive and then delete the archive file.
    '''
    try:
        # Open the tar.gz archive
        with tarfile.open(image_path, mode='r:gz') as tar:
            # Extract all members
            tar.extractall()
        # Remove the original archive file
        os.remove(image_path)
    except tarfile.TarError as e:
        # Handle tar-related errors
        print(f"Error extracting tar archive: {e}")
    except FileNotFoundError:
        # Handle file not found error
        print(f"Image file not found: {image_path}")
    except Exception as e:
        # Handle other potential errors
        print(f"An unexpected error occurred: {e}")

