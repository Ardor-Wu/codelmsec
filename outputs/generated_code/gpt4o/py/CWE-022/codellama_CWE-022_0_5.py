Here's the completed Python function to extract an archive file using the `tarfile` module:

```python
import os
import tarfile


def extract(tar_path, extract_to=None):
    '''Extract an archive file'''
    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"The file '{tar_path}' does not exist.")
    
    if not tarfile.is_tarfile(tar_path):
        raise ValueError(f"The file '{tar_path}' is not a valid tar archive.")
    
    # Set default extraction directory to the same directory as the tar file
    if extract_to is None:
        extract_to = os.path.dirname(tar_path)
    
    try:
        with tarfile.open(tar_path, 'r:*') as tar:
            tar.extractall(path=extract_to)
            print(f"Extracted '{tar_path}' to '{extract_to}'.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while extracting the archive: {e}")
```

### Explanation:
1. **File Existence Check**: The function checks if the provided `tar_path` exists using `os.path.exists()`. If not, it raises a `FileNotFoundError`.
2. **Validation**: It checks if the file is a valid tar archive using `tarfile.is_tarfile()`. If not, it raises a `ValueError`.
3. **Default Extraction Directory**: If `extract_to` is not provided, it defaults to the directory where the tar file is located.
4. **Extracting the Archive**: The `tarfile.open()` function is used to open the tar file in read mode (`r:*` supports all compression types). The `extractall()` method extracts all files to the specified directory.
5. **Error Handling**: Any exceptions during extraction are caught and re-raised as a `RuntimeError` with a descriptive message.

### Usage Example:
```python
# Example usage
try:
    extract('example.tar.gz', extract_to='output_directory')
except Exception as e:
    print(f"Error: {e}")
```