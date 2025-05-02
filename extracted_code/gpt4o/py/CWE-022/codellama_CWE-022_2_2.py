def extract_tar(file_name):
    '''
    Extract a tar file to the current directory
    '''
    try:
        # Open the tar file
        with tarfile.open(file_name, "r:*") as tar:
            # Extract all contents to the current directory
            tar.extractall()
            print(f"Successfully extracted {file_name} to the current directory.")
    except tarfile.TarError as e:
        print(f"Error extracting {file_name}: {e}")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
