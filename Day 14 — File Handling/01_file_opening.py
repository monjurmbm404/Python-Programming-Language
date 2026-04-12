"""
========================================
01_file_opening.py
========================================
File Opening:

✔ open() function is used to open files
✔ Syntax: open(filename, mode)
✔ Modes: r, w, a
"""

# Opening a file in read mode
file = open("sample.txt", "r")

# Read content
content = file.read()

print("File Content:")
print(content)

# Always close the file
file.close()