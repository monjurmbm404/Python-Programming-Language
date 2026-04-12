"""
========================================
05_raise_exception.py
========================================
raise keyword:

✔ Used to manually create exception
"""

age = -5

if age < 0:
    raise ValueError("Age cannot be negative!")

print("Age is valid")