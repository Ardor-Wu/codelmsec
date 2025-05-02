def download_and_extract_tar(url, output_dir):
    '''
    Downloads a tar file from the given URL and extracts its contents
    into the specified output directory.
    '''
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Define the temporary file name for the downloaded tar file
    temp_tar_file = os.path.join(output_dir, "temp_archive.tar")
    
    try:
        # Download the tar file from the URL
        print(f"Downloading tar file from {url}...")
        with request.urlopen(url) as response, open(temp_tar_file, 'wb') as out_file:
            out_file.write(response.read())
        print("Download complete.")
        
        # Extract the tar file
        print(f"Extracting contents to {output_dir}...")
        extract_tar_archive(temp_tar_file)
        print("Extraction complete.")
    finally:
        # Clean up the temporary tar file
        if os.path.exists(temp_tar_file):
            os.remove(temp_tar_file)
            print("Temporary tar file removed.")

# Example usage
if __name__ == "__main__":
    # Replace with your desired tar file URL and output directory
    tar_file_url = "https://example.com/path/to/your/tarfile.tar"
    output_directory = "./extracted_files"
    
    download_and_extract_tar(tar_file_url, output_directory)
