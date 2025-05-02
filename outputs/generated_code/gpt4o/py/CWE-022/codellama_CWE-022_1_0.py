Here is the completed Python code for the `extract_tar` function:

```python
import tarfile
import os
from urllib.request import urlopen


def extract_tar(file_name): 
    # Extract the tar file
    with tarfile.open(file_name, mode='r:*') as tar:
        # Extract all files to the current directory
        tar.extractall()
        print(f"Extracted all files from {file_name} to the current directory.")

# Example usage
if __name__ == "__main__":
    # Ensure the tar file exists before extracting
    tar_file = "example.tar"
    if os.path.exists(tar_file):
        extract_tar(tar_file)
    else:
        print(f"{tar_file} does not exist.")
```

### Explanation:
1. **`tarfile.open(file_name, mode='r:*')`**: Opens the tar file for reading. The `r:*` mode allows handling of both compressed and uncompressed tar files.
2. **`tar.extractall()`**: Extracts all files from the tar archive into the current working directory.
3. **Error Handling**: Before calling `extract_tar`, the code checks if the file exists using `os.path.exists()` to avoid errors.

You can modify the extraction path or handle specific files within the tar archive if needed.