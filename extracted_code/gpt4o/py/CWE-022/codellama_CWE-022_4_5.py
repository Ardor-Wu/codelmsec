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
