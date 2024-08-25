"""
MotiveProcessor Script

Author: Jaebeom Jo
Email: jojaebeom@gm.gist.ac.kr
"""

import os
import zipfile
import json

# Load configuration from config.json
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

BASE_DIR = config['BASE_DIR']
SUBJECT_NUM = config['SUBJECT_NUM']
folders_with_subfolders = config['folders_with_subfolders']
folders_without_subfolders = config['folders_without_subfolders']

def unzip_file(zip_file_path, extract_to_folder):
    """
    Unzips the specified file to the target folder.
    """
    if not os.path.isfile(zip_file_path):
        print(f"File does not exist: {zip_file_path}")
        return
    
    if not os.path.exists(extract_to_folder):
        os.makedirs(extract_to_folder)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_folder)
        print(f"Files have been extracted to {extract_to_folder}.")

def mk_folder(base_dir, subject_num, zip_file='Task_list.zip'):
    """
    Creates folders for the specified subject number and optionally unzips a task file.
    """
    print(f"Creating folder for Subject {subject_num:03} in {base_dir}...")
    
    subject_folder = os.path.join(base_dir, f"Subject{subject_num:03}")
    if not os.path.exists(subject_folder):
        os.makedirs(subject_folder)
        print(f"Created directory: {subject_folder}")
    
    user_input = input("Do you want to unzip the task file? (Y/n): ")
    if user_input.lower() in ['y', 'yes']:
        unzip_file(zip_file, subject_folder)
    else:
        print("Skipping unzipping of the task file.")

    print("")

if __name__ == "__main__":
    mk_folder(BASE_DIR, SUBJECT_NUM)
