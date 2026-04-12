"""
========================================
05_recursive_problem_solving.py
========================================
Recursive Problem Solving:

✔ Break problem into smaller sub-problems
"""

# Sum of numbers using recursion
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

print("Sum:", sum_numbers(5))


# Reverse string using recursion
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

text = "Python"
print("Reversed:", reverse_string(text))