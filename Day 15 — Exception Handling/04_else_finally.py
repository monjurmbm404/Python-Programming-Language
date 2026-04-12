"""
========================================
04_else_finally.py
========================================
else & finally:

✔ else → runs if no error
✔ finally → always runs
"""

try:
    num = 10
    result = num / 2

except ZeroDivisionError:
    print("Error occurred")

else:
    print("No error occurred:", result)

finally:
    print("This always runs (cleanup code)")