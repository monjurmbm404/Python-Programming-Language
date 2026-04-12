"""
========================================
04_write_append.py
========================================
Write & Append:

✔ write() overwrites file
✔ append() adds content
"""

# Write mode
with open("data.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Learning File Handling\n")

# Append mode
with open("data.txt", "a") as file:
    file.write("Adding more data...\n")

# Read file
with open("data.txt", "r") as file:
    print(file.read())