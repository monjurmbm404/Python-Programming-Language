"""
========================================
04_filter_function.py
========================================
filter() Function:

✔ Filters elements based on condition
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", evens)