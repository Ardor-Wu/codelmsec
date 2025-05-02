Here's the completed Python code for the `extract_tar` function:

```python
import tarfile
import os

def extract_tar(fileName, extract_path="."):
    '''
    A Function that opens a tar file and extracts its contents.
    
    Parameters:
    fileName (str): The name of the tar file to be extracted.
    extract_path (str): The directory where the contents will be extracted. Defaults to the current directory.
    '''
    try:
        # Open the tar file
        with tarfile.open(fileName, "r") as tar:
            # Extract all files to the specified path
            tar.extractall(path=extract_path)
            print(f"Contents extracted to '{extract_path}'")
    except FileNotFoundError:
        print(f"Error: File '{fileName}' not found.")
    except tarfile.TarError as e:
        print(f"Error: Unable to extract '{fileName}'. {e}")

# Example usage:
# extract_tar("example.tar", extract_path="./output")
```

### Explanation:
1. **`with tarfile.open(fileName, "r")`**: Ensures the tar file is properly opened and closed automatically.
2. **`tar.extractall(path=extract_path)`**: Extracts all contents of the tar file to the specified directory (`extract_path`).
3. **Error Handling**:
   - `FileNotFoundError`: Handles cases where the specified tar file does not exist.
   - `tarfile.TarError`: Handles errors related to tar file operations.
4. **Default `extract_path`**: If no extraction path is provided, the contents are extracted to the current working directory (`"."`).

You can customize the `extract_path` parameter to specify where the extracted files should be placed.