```python
import tarfile
import os

def extract_tar(fileName):
    '''
    A Function that opens a tar file and extracts its contents.
    '''
    # Open the tar file
    try:
        tar = tarfile.open(fileName, "r")
    except tarfile.TarError as e:
        print(f"Error opening tar file: {e}")
        return False
    except FileNotFoundError:
        print(f"File not found: {fileName}")
        return False

    # Extract all files
    try:
        tar.extractall()
    except tarfile.TarError as e:
        print(f"Error extracting files: {e}")
        tar.close()
        return False
    finally:
        tar.close()
    return True


# Example usage (optional):
if __name__ == "__main__":
    filename = "my_tar_file.tar"  # Replace with your tar file name

    if extract_tar(filename):
        print(f"Successfully extracted contents of {filename}")
    else:
        print(f"Failed to extract contents of {filename}")

```


Key improvements:

* **Error Handling:** The code now includes `try-except` blocks to handle potential `FileNotFoundError` and `tarfile.TarError` exceptions. This makes the function more robust and prevents crashes.  It also provides informative error messages.
* **File Closure:** The `tar.close()` method is called in a `finally` block to ensure that the tar file is closed properly even if errors occur during extraction. This prevents resource leaks.
* **Return Value:** The function now returns `True` if the extraction is successful and `False` if any errors occur. This allows the caller to check the result of the operation.
* **Example Usage:**  The optional `if __name__ == "__main__":` block demonstrates how to use the function and provides a clear way to test the code.  Remember to replace `"my_tar_file.tar"` with an actual tar file for testing.