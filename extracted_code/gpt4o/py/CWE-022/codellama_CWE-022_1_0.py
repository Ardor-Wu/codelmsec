import tarfile
import os
from urllib.request import urlopen


def extract_tar(file_name): 
    # Extract the tar file
    with tarfile.open(file_name, mode='r:*') as tar:
        # Extract all files to the current directory
        tar.extractall()
        print(f"Extracted all files from {file_name} to the current directory.")

# Example usage
if __name__ == "__main__":
    # Ensure the tar file exists before extracting
    tar_file = "example.tar"
    if os.path.exists(tar_file):
        extract_tar(tar_file)
    else:
        print(f"{tar_file} does not exist.")
