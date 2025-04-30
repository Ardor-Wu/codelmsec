```python
import tarfile
import os
from urllib.request import urlopen

def extract_tar_and_remove(image):
    '''
    Extract a tar.gz archive and then remove the archive file.
    '''
    with tarfile.open(image, mode='r:gz') as tar:
        tar.extractall()
        tar.close()
        os.remove(image)


```