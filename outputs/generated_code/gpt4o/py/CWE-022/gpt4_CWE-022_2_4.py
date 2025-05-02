Here is the completed `extract_content` function:

```python
def extract_content(file_name):
    '''
    Open a tar file and extract its contents
    '''
    if not tarfile.is_tarfile(file_name):
        raise ValueError(f"{file_name} is not a valid tar file.")
    
    with tarfile.open(file_name, 'r:*') as tar:
        extract_path = os.path.splitext(file_name)[0]  # Remove the file extension for the folder name
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)
        tar.extractall(path=extract_path)
        print(f"Contents extracted to {extract_path}")
```

### Explanation:
1. **Check if the file is a valid tar file**: The `tarfile.is_tarfile()` function is used to verify that the provided file is a valid tar archive.
2. **Open the tar file**: The `tarfile.open()` function is used to open the tar file in read mode (`'r:*'` allows reading any tar compression format).
3. **Create an extraction path**: The `os.path.splitext()` function is used to remove the file extension from the tar file name to create a directory for extraction. If the directory does not exist, it is created using `os.makedirs()`.
4. **Extract the contents**: The `tar.extractall()` function extracts all the contents of the tar file into the specified directory.
5. **Print a success message**: A message is printed to indicate where the contents were extracted.

You can now use this function to extract the contents of a tar file by providing its file name as an argument.