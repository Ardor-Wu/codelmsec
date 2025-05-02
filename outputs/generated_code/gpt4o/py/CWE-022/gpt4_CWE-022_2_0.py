```python
        # Extract all the content in the current working directory
        f.extractall()

def download_and_extract_tar(url, output_dir):
    """
    Download a tar file from a URL and extract its content
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Define the temporary file name for the downloaded tar file
    temp_tar_file = os.path.join(output_dir, "temp_download.tar")

    try:
        # Download the tar file
        with request.urlopen(url) as response:
            with open(temp_tar_file, 'wb') as out_file:
                out_file.write(response.read())

        # Change to the output directory
        os.chdir(output_dir)

        # Extract the tar file content
        extract_tar_content(temp_tar_file)

    finally:
        # Clean up the temporary tar file
        if os.path.exists(temp_tar_file):
            os.remove(temp_tar_file)

# Example usage
if __name__ == "__main__":
    tar_url = "https://example.com/path/to/your/tarfile.tar"  # Replace with the actual URL
    output_directory = "./extracted_files"  # Replace with your desired output directory

    download_and_extract_tar(tar_url, output_directory)
    print(f"Files have been extracted to: {output_directory}")
```