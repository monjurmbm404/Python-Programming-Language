"""
========================================
03_read_file.py
========================================
Reading Files:

✔ read() -> full file
✔ readline() -> one line
✔ readlines() -> list of lines
"""

file = open("demo.txt", "r")

# Read full file
print("Full Content:")
print(file.read())

file.close()

# Reading line by line
file = open("demo.txt", "r")

print("\nLine by Line:")
print(file.readline())
print(file.readline())

file.close()