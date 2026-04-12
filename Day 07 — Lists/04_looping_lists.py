"""
========================================
04_looping_lists.py
========================================
Looping Through Lists:

✔ Using for loop
✔ Using for-each style
"""

fruits = ["apple", "banana", "mango"]

# Normal loop
for i in range(len(fruits)):
    print("Index", i, ":", fruits[i])

print()

# Direct loop
for fruit in fruits:
    print("Fruit:", fruit)