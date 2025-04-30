```python
import tarfile
import os
from urllib.request import urlopen

def remove_tar(image):
    """
    Decompress the tar.gz file and remove the original file when decompression is finished.
    """
    # Open the tar archive in 'read and gzip' mode
    with tarfile.open(image, "r:gz") as tar:
        # Extract all members to the current directory
        tar.extractall()
    # Remove the original tar.gz file
    os.remove(image)


def download_and_extract(url, filename):
    """Downloads a tar.gz file and extracts it."""

    try:
        with urlopen(url) as response, open(filename, 'wb') as f:
            f.write(response.read())

        remove_tar(filename)
        print(f"Successfully downloaded and extracted {filename}")

    except Exception as e:
        print(f"Error downloading or extracting {filename}: {e}")


if __name__ == "__main__":
    # Example usage (replace with your desired URL and filename)
    example_url = "https://www.example.com/example.tar.gz"  # Replace with a real URL
    example_filename = "example.tar.gz"
    download_and_extract(example_url, example_filename)


```


Key improvements:

* **Error Handling:** The `download_and_extract` function now includes a `try...except` block to handle potential errors during download or extraction, providing more robust code.  This prevents the script from crashing and gives the user feedback.
* **Clearer output:**  Prints informative messages about success or failure.
* **Example Usage:** The `if __name__ == "__main__":` block provides a clear example of how to use the functions.  The comments clearly indicate that the example URL and filename should be replaced with real values.
* **Maintainability:** The code is more organized and easier to understand.


It's crucial to replace `"https://www.example.com/example.tar.gz"` with a valid URL of a `.tar.gz` file for testing.  Also, be aware that the code extracts files to the *current working directory*.  You might want to add functionality to specify an extraction directory for greater control.