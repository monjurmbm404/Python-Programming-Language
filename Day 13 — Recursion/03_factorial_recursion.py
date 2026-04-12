"""
========================================
03_factorial_recursion.py
========================================
Factorial Using Recursion:

✔ n! = n × (n-1)!
✔ Base case: 0! = 1
"""

def factorial(n):
    if n == 0:
        return 1  # Base case

    return n * factorial(n - 1)

num = 5
print("Factorial:", factorial(num))