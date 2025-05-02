import tarfile
import os
import json

def extract_json(json_archive_path):
    '''
    Extract the JSON data from the tar archive containing JSON files.
    
    Parameters:
        json_archive_path (str): Path to the tar archive file.
    
    Returns:
        list: A list of dictionaries containing the JSON data from the extracted files.
    '''
    extracted_data = []

    # Check if the file is a valid tar archive
    if tarfile.is_tarfile(json_archive_path):
        # Open the tar archive
        with tarfile.open(json_archive_path, 'r') as archive:
            # Iterate over each file in the archive
            for member in archive.getmembers():
                # Check if the file is a regular file and has a .json extension
                if member.isfile() and member.name.endswith('.json'):
                    # Extract the file
                    file = archive.extractfile(member)
                    if file:
                        # Load the JSON data from the file
                        try:
                            data = json.load(file)
                            extracted_data.append(data)
                        except json.JSONDecodeError:
                            print(f"Error decoding JSON in file: {member.name}")
                        finally:
                            file.close()
    else:
        print("The provided file is not a valid tar archive.")

    return extracted_data


json_archive_path = 'path/to/archive.tar'
data = extract_json(json_archive_path)
print(data)
