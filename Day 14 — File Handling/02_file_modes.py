"""
========================================
02_file_modes.py
========================================
File Modes:

✔ r -> read
✔ w -> write (overwrite)
✔ a -> append
"""

# Write mode (creates or overwrites file)
file = open("demo.txt", "w")
file.write("This is write mode.\n")
file.close()

# Append mode (adds content)
file = open("demo.txt", "a")
file.write("This is append mode.\n")
file.close()

# Read mode
file = open("demo.txt", "r")
print(file.read())
file.close()