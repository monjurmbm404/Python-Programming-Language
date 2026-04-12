"""
========================================
06_recursion_vs_loop.py
========================================
Recursion vs Loop:

✔ Both solve repeated tasks
✔ Loop = faster
✔ Recursion = cleaner logic
"""

# Factorial using loop
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Factorial using recursion
def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)

print("Loop Factorial:", factorial_loop(5))
print("Recursion Factorial:", factorial_rec(5))