"""
========================================
02_dictionary_comprehension.py
========================================
Dictionary Comprehension:

✔ Create dictionaries in one line
"""

# Normal way
square_dict = {}
for i in range(1, 6):
    square_dict[i] = i * i

print("Normal dict:", square_dict)

# Dictionary comprehension
square_dict2 = {i: i * i for i in range(1, 6)}

print("Dict comprehension:", square_dict2)

# Even numbers dictionary
even_dict = {i: i for i in range(1, 11) if i % 2 == 0}

print("Even dict:", even_dict)