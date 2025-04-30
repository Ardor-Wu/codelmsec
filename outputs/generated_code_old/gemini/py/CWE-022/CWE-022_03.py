```python
import tarfile
import os

def readArchive(fileName):
    '''
    Read the archive file and extract it to the current directory
    '''
    try:
        with tarfile.open(fileName, 'r') as tar:
            tar.extractall()
            print(f"Archive {fileName} extracted successfully.")
    except FileNotFoundError:
        print(f"Error: File {fileName} not found.")
    except tarfile.ReadError:
        print(f"Error: Could not read archive {fileName}. It may be corrupted or not a tar archive.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage (you can uncomment this to test):
# if __name__ == "__main__":
#     filename = "my_archive.tar.gz"  # Replace with your archive filename
#     readArchive(filename)

```


Key improvements:

* **Error Handling:** The code now includes robust error handling using `try...except` blocks. It catches `FileNotFoundError` if the archive doesn't exist, `tarfile.ReadError` if the file isn't