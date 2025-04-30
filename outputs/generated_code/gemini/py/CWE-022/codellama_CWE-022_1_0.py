```python
import tarfile
import os
from urllib.request import urlopen


def extract_tar(file_name): 
    # extract the tar file
    try:
        with tarfile.open(file_name, mode='r:*') as tar:
            tar.extractall()  # Extract all members to the current directory
        print(f"Successfully extracted {file_name}")
    except tarfile.TarError as e:
        print(f"Error extracting {file_name}: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_name}")

# Example usage (download and extract a tar.gz file):

url = "https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz"  # Example URL
filename = os.path.basename(url)

# Download the file (optional, if you already have the tar file locally, skip this)
try:
    with urlopen(url) as response, open(filename, 'wb') as outfile:
        outfile.write(response.read())
    print(f"Downloaded {filename}")
except Exception as e:
    print(f"Error downloading {filename}: {e}")


extract_tar(filename)


# Cleanup (optional): Remove the downloaded tar file.
# os.remove(filename) 
```



Key improvements and explanations:

1. **Error Handling:** The code now includes `try...except` blocks to handle potential errors like `tarfile.TarError` (if the tar file is corrupted) and `FileNotFoundError` (if the file doesn't exist). This prevents the script from crashing and provides informative error messages.

2. **`tar.extractall()`:**  The simplest and most common way to extract all members of a tar archive is to use `tar.extractall()`. It extracts everything to the current working directory by default.  You can optionally provide a `path` argument to `extractall(path="target_directory")` to extract to a specific directory.

3. **Example Download:** The code now includes an optional section that demonstrates how to download a tar.gz file from a URL using `urllib.request.urlopen()` before extracting it. This makes the example more complete and practical.

4. **Clearer output:**