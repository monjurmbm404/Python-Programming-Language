"""
========================================
03_multiple_except.py
========================================
Multiple except blocks:

✔ Handle different errors separately
"""

try:
    num = int("abc")  # ValueError
    result = 10 / 0   # ZeroDivisionError

except ValueError:
    print("Invalid value conversion!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Program finished")