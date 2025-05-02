import tarfile
import os

def extract_tar_file(fileName, extract_path="."):
    """
    Open the tarfile in read mode, extract all its contents to the specified path, 
    and close the tar file after extraction.
    
    Parameters:
    fileName (str): The path to the tar file to be extracted.
    extract_path (str): The directory where the contents will be extracted. Defaults to the current directory.
    """
    if not os.path.exists(fileName):
        raise FileNotFoundError(f"The file '{fileName}' does not exist.")
    
    if not tarfile.is_tarfile(fileName):
        raise tarfile.TarError(f"The file '{fileName}' is not a valid tar file.")
    
    try:
        with tarfile.open(fileName, "r") as tar:
            tar.extractall(path=extract_path)
            print(f"Contents extracted successfully to '{extract_path}'.")
    except Exception as e:
        print(f"An error occurred while extracting the tar file: {e}")


# Extract a tar file to the current directory
extract_tar_file("example.tar")

# Extract a tar file to a specific directory
extract_tar_file("example.tar", extract_path="output_directory")
