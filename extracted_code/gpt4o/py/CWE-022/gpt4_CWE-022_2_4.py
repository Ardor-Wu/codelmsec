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
