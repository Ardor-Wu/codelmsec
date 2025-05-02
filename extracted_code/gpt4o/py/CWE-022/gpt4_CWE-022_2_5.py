f.extractall()
        print(f"Extracted all files from {file_name}")

def download_and_extract(url, output_dir):
    """
    Download a tar file from a URL and extract its contents to a specified directory
    """
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Define the local file path for the downloaded tar file
        file_name = os.path.join(output_dir, os.path.basename(url))

        # Download the tar file
        print(f"Downloading {url}...")
        with request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded {file_name}")

        # Extract the tar file
        print(f"Extracting {file_name}...")
        untar(file_name)

        # Optionally, delete the tar file after extraction
        os.remove(file_name)
        print(f"Deleted the tar file {file_name} after extraction.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# url = "https://example.com/path/to/your/file.tar.gz"
# output_dir = "./output"
# download_and_extract(url, output_dir)
