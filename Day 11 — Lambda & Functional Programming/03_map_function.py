"""
========================================
03_map_function.py
========================================
map() Function:

✔ Applies a function to every element
✔ Returns new iterable
"""

numbers = [1, 2, 3, 4, 5]

# Using lambda with map
squares = list(map(lambda x: x * x, numbers))

print("Original:", numbers)
print("Squares:", squares)