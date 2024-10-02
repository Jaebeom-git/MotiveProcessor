"""
MotiveProcessor Script

Author: Jaebeom Jo
Email: jojaebeom@gm.gist.ac.kr
"""

import os
import json
import shutil

# Load configuration from config.json
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

BASE_DIR = config['BASE_DIR']
SUBJECT_NUM = config['SUBJECT_NUM']

# Define source and destination paths
subject_path = os.path.join(BASE_DIR, f"Subject{SUBJECT_NUM:03}")
raw_path = os.path.join(subject_path, 'Raw')

# Create Raw folder if it doesn't exist
if not os.path.exists(raw_path):
    os.makedirs(raw_path)

# Iterate over all items (folders) in the SUBJECT_NUM directory
for item in os.listdir(subject_path):
    item_path = os.path.join(subject_path, item)

    # Only move directories, skip the Raw folder itself
    if os.path.isdir(item_path) and item != 'Raw':
        # Move the folder to the Raw folder
        dest_path = os.path.join(raw_path, item)
        shutil.move(item_path, dest_path)

print(f"Moved to {raw_path}")
