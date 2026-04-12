"""
========================================
05_file_pointer.py
========================================
File Pointer:

✔ tell() -> current position
✔ seek() -> move pointer
"""

with open("data.txt", "r") as file:

    print("Initial position:", file.tell())

    print("Reading first 5 characters:", file.read(5))
    print("Position after read:", file.tell())

    # Move pointer back to start
    file.seek(0)

    print("After seek(0):", file.read())