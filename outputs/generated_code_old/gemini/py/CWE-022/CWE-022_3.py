```python
import tarfile

def extract_tar(tar_path, dest_dir):
    """
    Extract files from a tar archive to a specified directory.
    """
    # Open the tar archive
    tar = tarfile.open(tar_path)

    # Iterate over the files in the tar archive
    for tarinfo in tar:
        tar.extract(tarinfo, path=dest_dir)

    # Close the tar archive
    tar.close()



import os
import tarfile

def extract_files(tar_path, dest_dir):
    """
    Extract files from a tar archive to the current working directory.
    """
    with tarfile.open(tar_path) as f:
        f.extractall(path=dest_dir)



import json
import urllib.request as request
import tarfile
import os

def extract_zip(file_name):
    """
    Extract files from a tar archive to the current working directory.
    """
    with tarfile.open(file_name) as f:
        f.extractall()



import tarfile
import os
from urllib.request import urlopen

def extract(image):
    ''' 
    Extract a tar.gz image and then remove the original archive.
    '''
    with tarfile.open(image, mode='r:gz') as tar:
        tar.extractall()
        tar.close()
        os.remove(image)



import tarfile
import os

def extract_tar_all(fileName):
    """
    Extract all files from a tar archive to the current working directory.
    """
    tar = tarfile.open(fileName, "r")
    tar.extractall()
    tar.close()

```