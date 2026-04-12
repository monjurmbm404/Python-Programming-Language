"""
========================================
04_os_module.py
========================================
os Module:

✔ Used for file and folder operations
"""

import os

# Current working directory
print("Current Directory:", os.getcwd())

# List files in directory
print("Files:", os.listdir())

# Create folder
if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
    print("Folder created")

# Remove folder (optional)
# os.rmdir("test_folder")