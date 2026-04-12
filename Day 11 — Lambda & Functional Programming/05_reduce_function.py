"""
========================================
05_reduce_function.py
========================================
reduce() Function:

✔ Found in functools module
✔ Reduces list to single value
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum using reduce
result = reduce(lambda x, y: x + y, numbers)

print("Sum:", result)

# Product using reduce
product = reduce(lambda x, y: x * y, numbers)

print("Product:", product)