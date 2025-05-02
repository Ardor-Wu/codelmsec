```python
    # Using `tarfile.open` to open the tar file
    tar = tarfile.open(fileName, "r")
    
    # Extract all the contents of the tar file
    tar.extractall()
    
    # Close the tar file
    tar.close()
    
    print(f"All files have been extracted from {fileName}")

# Example usage
if __name__ == "__main__":
    fileName = "example.tar"  # Replace with your tar file name
    if os.path.exists(fileName):
        untar_file(fileName)
    else:
        print(f"The file {fileName} does not exist.")
```