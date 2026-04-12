"""
========================================
01_list_comprehension.py
========================================
List Comprehension:

✔ Short way to create lists
✔ Faster and cleaner than loops
"""

# Normal way
numbers = []
for i in range(1, 6):
    numbers.append(i)

print("Normal list:", numbers)

# List comprehension
numbers2 = [i for i in range(1, 6)]

print("List comprehension:", numbers2)

# Squares
squares = [i * i for i in range(1, 6)]
print("Squares:", squares)

# Even numbers
evens = [i for i in range(1, 11) if i % 2 == 0]
print("Even numbers:", evens)