```python
import json
import urllib.request as request
import tarfile
import os

def extract_content(file_name):
    '''
    Open a tar file and extract its contents
    '''
    try:
        with tarfile.open(file_name, 'r') as tar:
            tar.extractall()
            print(f"Successfully extracted contents of {file_name}")
    except tarfile.TarError as e:
        print(f"Error extracting tar file: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

```