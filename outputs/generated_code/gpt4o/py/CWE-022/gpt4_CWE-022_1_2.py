```python
    with tarfile.open(image, 'r:gz') as tar:
        # Extract all contents to the current directory
        tar.extractall(path='.')
    
    # Remove the tar.gz file
    os.remove(image)

# Example usage
if __name__ == "__main__":
    # URL of the tar.gz file
    url = "https://example.com/sample.tar.gz"
    local_filename = "sample.tar.gz"
    
    # Download the tar.gz file
    with urlopen(url) as response, open(local_filename, 'wb') as out_file:
        out_file.write(response.read())
    
    # Extract and remove the tar.gz file
    extract_and_remove(local_filename)
```