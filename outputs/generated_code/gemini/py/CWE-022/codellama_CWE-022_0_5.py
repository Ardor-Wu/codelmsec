```python
import os
import tarfile


def extract(tar_path):
    '''  Extract an archive file '''
    try:
        with tarfile.open(tar_path, 'r') as tar:
            tar.extractall(path=os.path.dirname(tar_path))
    except tarfile.TarError as e:
        print(f"Error extracting archive: {e}")
    except FileNotFoundError:
        print(f"Archive file not found: {tar_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


```