import tarfile
import os
from urllib.request import urlopen

def extract_and_delete_tar(image):
    """
    This function performs two actions:
    1. Opens the tar archive with the image and performs extraction to the current directory.
    2. Removes the tar image file after extraction.
    
    Parameters:
    image (str): The path to the tar file to be extracted.
    """
    try:
        # Check if the file exists
        if not os.path.exists(image):
            print(f"Error: The file '{image}' does not exist.")
            return
        
        # Open the tar file
        with tarfile.open(image, 'r') as tar:
            # Extract all contents to the current directory
            print(f"Extracting contents of '{image}'...")
            tar.extractall()
            print(f"Extraction completed.")
        
        # Delete the tar file
        print(f"Deleting the tar file '{image}'...")
        os.remove(image)
        print(f"File '{image}' has been deleted.")
    
    except tarfile.TarError as e:
        print(f"Error: Unable to process the tar file. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Assuming 'example.tar' is a tar file in the current directory
extract_and_delete_tar('example.tar')
