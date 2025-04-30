```python
import tarfile
import os
from urllib.request import urlopen

def extract(image):
    ''' 
    Extract the image to the appropriate directory
    '''
    filename = image.split('/')[-1]
    filepath = os.path.join("data", filename)

    # Download if the file doesn't exist
    if not os.path.exists(filepath):
        print(f"Downloading {image} to {filepath}")
        with urlopen(image) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())

    # Extract the tar file
    if filename.endswith(".tgz") or filename.endswith(".tar.gz"):
        try:
            with tarfile.open(filepath, "r:gz") as tar:
                extract_dir = os.path.join("data", filename.split('.')[0])  # Extract to a directory named after the file
                if not os.path.exists(extract_dir):
                    os.makedirs(extract_dir)
                print(f"Extracting {filename} to {extract_dir}")
