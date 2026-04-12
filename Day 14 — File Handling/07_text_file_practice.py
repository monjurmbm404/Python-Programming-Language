"""
========================================
07_text_file_practice.py
========================================
Working with Text Files:

✔ Real-world file handling example
"""

# Write multiple lines
with open("notes.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("Day 14 Learning\n")
    file.write("Practice is important\n")

# Read and process file
with open("notes.txt", "r") as file:
    lines = file.readlines()

print("Total Lines:", len(lines))

for line in lines:
    print("Line:", line.strip())