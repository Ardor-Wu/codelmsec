tar:
            tar.extractall()
            print(f"Extracted all files from {file_name} into the current directory.")

def download_and_unpack_tarball(url, output_file):
    '''
    Downloads a tarball from the given URL and unpacks it in the current directory.
    '''
    try:
        # Download the tarball
        print(f"Downloading tarball from {url}...")
        with request.urlopen(url) as response, open(output_file, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded tarball to {output_file}.")

        # Unpack the tarball
        unpack_tarball(output_file)

        # Optionally, delete the tarball after extraction
        os.remove(output_file)
        print(f"Deleted the tarball file {output_file} after extraction.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    tarball_url = "https://example.com/path/to/your/tarball.tar.gz"
    output_file_name = "downloaded_tarball.tar.gz"
    download_and_unpack_tarball(tarball_url, output_file_name)
