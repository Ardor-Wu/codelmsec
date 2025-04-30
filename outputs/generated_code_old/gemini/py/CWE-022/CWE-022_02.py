```python
import json
import urllib.request as request
import tarfile
import os

def extract_zip(file_name):
    """Extracts a tar or zip archive.

    Args:
        file_name: The path to the archive file.
    """
    try:
        if file_name.endswith(".tar.gz") or file_name.endswith(".tgz"):
            with tarfile.open(file_name, "r:gz") as tar:
                tar.extractall(path=os.path.dirname(file_name))
        elif file_name.endswith(".tar"):
            with tarfile.open(file_name, "r:") as tar:
                tar.extractall(path=os.path.dirname(file_name))
        elif file_name.endswith(".zip"):
            import zipfile  # Import zipfile only if needed
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall(path=os.path.dirname(file_name))
        else:
            raise ValueError("Unsupported archive format. Only .tar.gz, .