'''
    After extraction, the function returns a list of the extracted file paths.
    
    Parameters:
        tar_path (str): Path to the tar archive file.
        dest_dir (str): Path to the destination directory where files will be extracted.
    
    Returns:
        list: A list of file paths of the extracted files.
    '''
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)  # Create destination directory if it doesn't exist
    
    extracted_files = []
    try:
        with tarfile.open(tar_path, 'r') as tar:
            tar.extractall(path=dest_dir)  # Extract all files to the destination directory
            extracted_files = [os.path.join(dest_dir, member.name) for member in tar.getmembers() if member.isfile()]
    except (tarfile.TarError, FileNotFoundError) as e:
        print(f"Error extracting tar file: {e}")
    
    return extracted_files

# Example usage:
# tar_path = 'example.tar'
# dest_dir = 'extracted_files'
# extracted_files = extract_tar_files(tar_path, dest_dir)
# print("Extracted files:", extracted_files)
