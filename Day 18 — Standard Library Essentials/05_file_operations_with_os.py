"""
========================================
05_file_operations_with_os.py
========================================
File Operations using os:

✔ Check file exists
✔ Rename file
✔ Delete file
"""

import os

file_name = "sample.txt"

# Check file exists
if os.path.exists(file_name):
    print("File exists")
else:
    print("File not found")

# Create file
with open(file_name, "w") as f:
    f.write("Hello Python OS Module")

# Rename file
os.rename(file_name, "renamed_sample.txt")
print("File renamed")

# Delete file
# os.remove("renamed_sample.txt")