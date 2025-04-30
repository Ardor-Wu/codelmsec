```python
import tarfile

def extract_tar(file_name):
    """Extract all files from a tar archive."""
    with tarfile.open(file_name) as f:
        f.extractall()


import json
import urllib.request as request
import tarfile
import os

def extract_zip(file_name):
    """Extract all files from a zip archive."""
    with tarfile.open(file_name) as f:  # Assuming file_name is actually a tar archive
        f.extractall()


import tarfile
import os
from urllib.request import urlopen

def extract(image):
    ''' 
    Extract the image to the appropriate directory
    '''
    with tarfile.open(image, mode='r:gz') as tar:
        tar.extractall()
        tar.close()
        os.remove(image)


import tarfile
import os

def readArchive(fileName):
    '''
    Read the archive file and extract it to the current directory
    '''
    tar = tarfile.open(fileName, "r")
    tar.extractall()
    tar.close()


import os
import tarfile

def extract_tar_to_dir(tar_path, dest_dir):
    """Extract all files from a tar archive to a specified directory."""
    # Open the tar archive
    tar = tarfile.open(tar_path)

    # Iterate over the files in the tar archive
    for tarinfo in tar:
       tar.extract(tarinfo, path=dest_dir)

    # Close the tar archive
    tar.close()

```