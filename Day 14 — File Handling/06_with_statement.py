"""
========================================
06_with_statement.py
========================================
with Statement:

✔ Automatically closes file
✔ Best practice
"""

with open("example.txt", "w") as file:
    file.write("Using with statement\n")

# No need to manually close file

with open("example.txt", "r") as file:
    print(file.read())