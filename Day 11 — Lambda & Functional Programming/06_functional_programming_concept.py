"""
========================================
06_functional_programming_concept.py
========================================
Functional Programming Concept:

✔ Focus on functions
✔ No side effects (pure functions)
✔ Uses map, filter, reduce
"""

numbers = [1, 2, 3, 4, 5]

# Step 1: Square all numbers
squares = list(map(lambda x: x * x, numbers))

# Step 2: Filter even squares
even_squares = list(filter(lambda x: x % 2 == 0, squares))

print("Original:", numbers)
print("Squares:", squares)
print("Even Squares:", even_squares)