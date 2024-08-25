import shutil
import os
import json

# Load configuration from config.json
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

# Assign configuration values to variables
BASE_DIR = config['BASE_DIR']
SUBJECT_NUM = config['SUBJECT_NUM']
folders_with_subfolders = config['folders_with_subfolders']
folders_without_subfolders = config['folders_without_subfolders']

def move_tak_files_to_named_folders(base_dir, subject_num):
    """
    Moves .tak files from the subject folder into specific subfolders
    based on their filenames.
    """
    # Define the path to the subject's folder
    subject_folder = os.path.join(base_dir, f"Subject{subject_num:03}")

    # Check if the subject folder exists
    if not os.path.exists(subject_folder):
        print(f"Subject folder {subject_folder} does not exist.")
        return
    
    # Iterate through files in the subject folder
    for file in os.listdir(subject_folder):
        if file.endswith('.tak'):
            file_path = os.path.join(subject_folder, file)
            
            # Determine the target folder name
            if 'Calibration' in file:
                folder_name = "Calibration"
            else:
                # Use the filename without extension as the folder name
                folder_name = os.path.splitext(file)[0]
            
            target_folder = os.path.join(subject_folder, folder_name)
            
            # Create the target folder if it does not exist
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
                print(f"Created folder: {target_folder}")
            
            # Move the .tak file to the target folder
            shutil.move(file_path, os.path.join(target_folder, file))
            print(f"Moved file {file} to folder {target_folder}")

# Call the function to move .tak files using the configured BASE_DIR and SUBJECT_NUM
move_tak_files_to_named_folders(BASE_DIR, SUBJECT_NUM)
