"""
========================================
02_try_except.py
========================================
try-except:

✔ try → risky code
✔ except → handles error
"""

try:
    a = 10
    b = 0
    result = a / b
    print(result)

except:
    print("Error occurred: Cannot divide by zero")

print("Program continues...")