```python
import json
import urllib.request as request
import tarfile
import os

import shutil

def extract_tar(file_name):
    '''
        Extract a tar file to the current directory
        '''    # Initialize the tar object
    try:
        with tarfile.open(file_name, 'r') as tar:
            # Extract all members to the current directory
            tar.extractall()
    except (FileNotFoundError, tarfile.ReadError) as e:
        print(f"Error extracting {file_name}: {e}")
        return False
    return True


def download_file(url, output_path):
    '''Downloads a file from the given url to the specified output path'''
    try:
        request.urlretrieve(url, output_path)
        return True
    except Exception as e:
        print(f"Error downloading file from {url}: {e}")
        return False


def prepare_dataset(config_path):
    '''Prepare the dataset for model training'''
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Error: Config file {config_path} not found")
        return

    data_url = config.get('data_url')
    dataset_name = config.get('dataset_name')
    extracted_dir = config.get("extracted_dir", dataset_name)  # Default to dataset_name if not specified


    if not data_url or not dataset_name:
        print("Error: 'data_url' and 'dataset_name' must be specified in the config file.")
        return

    tar_file = f"{dataset_name}.tar.gz"  # Corrected to create expected filename
    if not download_file(data_url, tar_file):
        return

    if not extract_tar(tar_file):
        return


    # Remove the .tar.gz file
    os.remove(tar_file)


    if extracted_dir != dataset_name and os.path.exists(dataset_name): # Allow specifying a different extraction dir
        if os.path.exists(extracted_dir): # Don't overwrite if already there
            shutil.