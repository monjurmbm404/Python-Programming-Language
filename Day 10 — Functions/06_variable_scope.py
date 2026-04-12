"""
========================================
06_variable_scope.py
========================================
Variable Scope:

✔ Local variable = inside function
✔ Global variable = outside function
"""

x = 100  # global variable

def demo():
    y = 50  # local variable
    print("Inside function (y):", y)
    print("Access global (x):", x)

demo()

print("Outside function (x):", x)

# print(y) ❌ Error: y is local to function