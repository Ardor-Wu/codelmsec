import tarfile
import os
from urllib.request import urlopen

def download_and_extract_tar_gz(url, destination_folder):
    """
    This function downloads a tar.gz file from a given URL, extracts all archived files
    into a specified destination folder, and deletes the tar.gz file after extraction.

    Parameters:
    - url (str): The URL of the tar.gz file to download.
    - destination_folder (str): The folder where the extracted files will be stored.
    """
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Define the name of the tar.gz file to be saved locally
    tar_gz_filename = os.path.join(destination_folder, "downloaded_file.tar.gz")

    try:
        # Download the tar.gz file
        print(f"Downloading file from {url}...")
        with urlopen(url) as response, open(tar_gz_filename, 'wb') as out_file:
            out_file.write(response.read())
        print(f"File downloaded and saved as {tar_gz_filename}")

        # Open the tar.gz file and extract its contents
        print(f"Extracting contents of {tar_gz_filename}...")
        with tarfile.open(tar_gz_filename, "r:gz") as tar:
            tar.extractall(path=destination_folder)
        print(f"Files extracted to {destination_folder}")

    finally:
        # Delete the tar.gz file after extraction
        if os.path.exists(tar_gz_filename):
            os.remove(tar_gz_filename)
            print(f"Deleted temporary file: {tar_gz_filename}")

# Example usage:
# download_and_extract_tar_gz("https://example.com/sample.tar.gz", "./extracted_files")
