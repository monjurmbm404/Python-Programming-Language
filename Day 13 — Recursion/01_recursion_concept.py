"""
========================================
01_recursion_concept.py
========================================
Recursion Concept:

✔ A function that calls itself
✔ Must have a base case (stop condition)
✔ Without base case → infinite loop
"""

def greet(n):
    if n == 0:  # Base case
        return
    print("Hello Recursion")
    greet(n - 1)  # Recursive call

greet(5)