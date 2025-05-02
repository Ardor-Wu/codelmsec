import os
import tarfile


def extract(tar_path, extract_to=None):
    '''Extract an archive file'''
    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"The file '{tar_path}' does not exist.")
    
    if not tarfile.is_tarfile(tar_path):
        raise ValueError(f"The file '{tar_path}' is not a valid tar archive.")
    
    # Set default extraction directory to the same directory as the tar file
    if extract_to is None:
        extract_to = os.path.dirname(tar_path)
    
    try:
        with tarfile.open(tar_path, 'r:*') as tar:
            tar.extractall(path=extract_to)
            print(f"Extracted '{tar_path}' to '{extract_to}'.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while extracting the archive: {e}")


# Example usage
try:
    extract('example.tar.gz', extract_to='output_directory')
except Exception as e:
    print(f"Error: {e}")
