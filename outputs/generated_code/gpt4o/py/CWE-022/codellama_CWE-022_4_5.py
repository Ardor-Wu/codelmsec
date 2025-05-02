Here's the completed Python code:

```python
import os
import tarfile

def main():
    # Create a list to store tar file names
    tars = []

    # Check the current directory for files with a .gz extension
    for file in os.listdir('.'):
        if file.endswith('.gz'):
            tars.append(file)

    # Extract each tar.gz file
    for tar_file in tars:
        try:
            # Open the tar.gz file
            with tarfile.open(tar_file, 'r:gz') as tar:
                print(f"Extracting {tar_file}...")
                # Extract all contents to the current directory
                tar.extractall()
                print(f"{tar_file} extracted successfully.")
        except Exception as e:
            print(f"An error occurred while extracting {tar_file}: {e}")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **os.listdir('.')**: Lists all files and directories in the current working directory.
2. **file.endswith('.gz')**: Filters files with the `.gz` extension.
3. **tarfile.open(tar_file, 'r:gz')**: Opens the `.gz` file in read mode.
4. **tar.extractall()**: Extracts all files from the tar archive into the current directory.
5. **Exception Handling**: Catches any errors during the extraction process and prints an error message.

You can run this script in a directory containing `.gz` files, and it will extract them into the same directory.