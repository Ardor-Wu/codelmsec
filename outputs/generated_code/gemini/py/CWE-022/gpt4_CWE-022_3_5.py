```python
import tarfile
import os

def download_and_extract(fileName):
    '''
    This function takes the path of tar file as an input, 
    then it extracts all the content from the file and 
    keeps it in the same directory.
    '''
    try:
        with tarfile.open(fileName, 'r') as tar:
            tar.extractall(path=os.path.dirname(fileName))
    except FileNotFoundError:
        print(f"Error: File '{fileName}' not found.")
    except tarfile.TarError as e:
        print(f"Error extracting tar file: {e}")

```