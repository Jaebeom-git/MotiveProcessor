"""
MotiveProcessor Script

Author: Jaebeom Jo
Email: jojaebeom@gm.gist.ac.kr
"""

import subprocess
import os
import xml.etree.ElementTree as ET
import json

# Load configuration from config.json
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

BASE_DIR = config['BASE_DIR']
SUBJECT_NUM = config['SUBJECT_NUM']
folders_with_subfolders = config['folders_with_subfolders']
folders_without_subfolders = config['folders_without_subfolders']

def update_csv_exporter_filename(xml_path, new_filename):
    """
    Updates the CSV exporter filename in the specified XML file.

    Args:
        xml_path (str): The path to the XML file to be updated.
        new_filename (str): The new filename to set in the XML configuration.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # Locate the property for the CSVExporterFilename and update its value
    for prop in root.findall(".//property"):
        if prop.find("name").text == "CSVExporterFilename":
            prop.find("value").text = new_filename
            break
    
    # Save the updated XML file
    tree.write(xml_path, encoding="UTF-8", xml_declaration=True)

def process_files_in_folder(folder_path, xml_path):
    """
    Processes all .tak files in the specified folder, updating the XML file for each file.

    Args:
        folder_path (str): The path to the folder containing .tak files.
        xml_path (str): The path to the XML file to be updated for each .tak file.
    """
    for file in os.listdir(folder_path):
        if file.endswith('.tak'):
            file_path = os.path.join(folder_path, file)
            
            # Set the path for the new CSV file based on the .tak file's name
            path, full_filename = os.path.split(file_path)
            filename_no_extension, _ = os.path.splitext(full_filename)
            new_csv_filename = os.path.join(path, filename_no_extension + ".csv")
            
            # Update the XML file with the new CSV filename
            update_csv_exporter_filename(xml_path, new_csv_filename)
            
            # Run the external script to process the folder
            subprocess.run(['python', '_process_folder_script.py', folder_path])

def export_tak(base_dir, subject_num):
    """
    Exports .tak files from the specified subject folder to CSV using the given XML configuration.

    Args:
        base_dir (str): The base directory where subject folders are located.
        subject_num (int): The subject number to identify the subject folder.
    """
    subject_folder = os.path.join(base_dir, f"Subject{subject_num:03}")
    xml_path = r'C:\ProgramData\OptiTrack\MotiveProfile.xml'
    
    # Process .tak files in folders without subfolders
    for folder in folders_without_subfolders:
        folder_path = os.path.join(subject_folder, folder)
        if os.path.exists(folder_path):
            process_files_in_folder(folder_path, xml_path)
    
    # Process .tak files in folders with subfolders
    for folder in folders_with_subfolders:
        for i in range(3):
            sub_folder_name = f"{folder}_{i:03}"
            folder_path = os.path.join(subject_folder, sub_folder_name)
            if os.path.exists(folder_path):
                process_files_in_folder(folder_path, xml_path)

# Call the export_tak function using the configured BASE_DIR and SUBJECT_NUM
export_tak(BASE_DIR, SUBJECT_NUM)
