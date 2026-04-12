"""
========================================
05_comprehension_with_condition.py
========================================
Comprehension with Conditions:

✔ Filtering + transformation together
"""

# Squares of even numbers only
result = [i * i for i in range(1, 11) if i % 2 == 0]

print("Squares of evens:", result)

# Words filtering
words = ["apple", "banana", "cherry", "kiwi"]

filtered = [word.upper() for word in words if len(word) > 5]

print("Filtered words:", filtered)