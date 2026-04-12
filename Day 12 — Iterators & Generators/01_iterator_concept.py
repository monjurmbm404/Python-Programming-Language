"""
========================================
01_iterator_concept.py
========================================
Iterator Concept:

✔ Iterator = object that allows traversal
✔ Used to loop through data one item at a time
✔ Uses __iter__() and __next__()
"""

numbers = [10, 20, 30, 40]

# Convert list to iterator
iterator = iter(numbers)

print("Iterator created")

# Manually accessing elements
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))