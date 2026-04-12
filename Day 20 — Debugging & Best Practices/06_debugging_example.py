"""
========================================
06_debugging_example.py
========================================
Debugging Example:

✔ Find bug step-by-step
"""

def divide_numbers(a, b):
    print("Debug: a =", a)
    print("Debug: b =", b)

    if b == 0:
        print("Error: Cannot divide by zero")
        return None

    result = a / b
    print("Debug result:", result)

    return result

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))