```python
import os
import tarfile

def extract_tar_files(tar_path, dest_dir):
    '''
    Open the provided tar archive file and extract each of the files it contains.
    These files are placed in a specified destination directory.
    After extraction, the tar archive file is deleted.
    '''
    try:
        # Open the tar archive file in read mode ('r')
        with tarfile.open(tar_path, 'r') as tar:
            # Extract all members to the destination directory
            tar.extractall(dest_dir)

    except FileNotFoundError:
        print(f"Error: Tar file not found at '{tar_path}'")
        return  # Exit early if file not found
    except tarfile.TarError as e:
        print(f"Error extracting tar file: {e}")
        return # Exit early if extraction fails
    finally:
        # Ensure the tar file is deleted whether or not an exception occurred.
        try:
            os.remove(tar_path)
        except FileNotFoundError:
            pass #Ignore if the file wasn't there (perhaps already deleted or exception prevented creation)


```