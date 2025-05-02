gz') as tar:
        # Extract all contents of the tar archive
        tar.extractall(path=os.path.dirname(image))
    
    # Remove the tar archive file
    os.remove(image)

def download_and_process_tar(url, destination):
    '''
    Downloads a tar archive from a URL, saves it to the destination, 
    extracts its contents, and removes the archive file
    '''
    # Download the tar archive
    response = urlopen(url)
    tar_data = response.read()

    # Save the tar archive to the destination
    with open(destination, 'wb') as file:
        file.write(tar_data)

    # Extract and remove the tar archive
    extract_and_remove_tar(destination)

# Example usage:
# url = "https://example.com/path/to/archive.tar.gz"
# destination = "/path/to/save/archive.tar.gz"
# download_and_process_tar(url, destination)
