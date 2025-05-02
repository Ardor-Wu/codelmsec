import tarfile
import os

def extract_tar(fileName, extract_path="."):
    '''
    A Function that opens a tar file and extracts its contents.
    
    Parameters:
    fileName (str): The name of the tar file to be extracted.
    extract_path (str): The directory where the contents will be extracted. Defaults to the current directory.
    '''
    try:
        # Open the tar file
        with tarfile.open(fileName, "r") as tar:
            # Extract all files to the specified path
            tar.extractall(path=extract_path)
            print(f"Contents extracted to '{extract_path}'")
    except FileNotFoundError:
        print(f"Error: File '{fileName}' not found.")
    except tarfile.TarError as e:
        print(f"Error: Unable to extract '{fileName}'. {e}")

# Example usage:
# extract_tar("example.tar", extract_path="./output")
