.open(image, 'r:gz') as tar:
        # Extract all the contents of the tar file into the current directory
        tar.extractall(path=os.path.dirname(image))
    
    # Remove the original tar.gz file after extraction
    os.remove(image)

# Example usage:
# Assuming you have a tar.gz file named 'example.tar.gz' in the current directory
# remove_tar('example.tar.gz')
