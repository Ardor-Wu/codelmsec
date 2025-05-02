import tarfile
import os

def download_and_extract(fileName):
    '''
    This function takes the path of a tar file as an input, 
    then it extracts all the content from the file and 
    keeps it in the same directory.
    '''
    # Check if the file exists
    if not os.path.exists(fileName):
        print(f"Error: File '{fileName}' does not exist.")
        return
    
    # Check if the file is a tar file
    if not tarfile.is_tarfile(fileName):
        print(f"Error: File '{fileName}' is not a valid tar file.")
        return
    
    try:
        # Open the tar file
        with tarfile.open(fileName, 'r') as tar:
            # Get the directory where the tar file is located
            extract_path = os.path.dirname(fileName)
            
            # Extract all contents to the same directory
            tar.extractall(path=extract_path)
            print(f"Contents extracted successfully to '{extract_path}'.")
    except Exception as e:
        print(f"An error occurred while extracting the tar file: {e}")


# Example tar file path
tar_file_path = "example.tar"

# Call the function
download_and_extract(tar_file_path)
