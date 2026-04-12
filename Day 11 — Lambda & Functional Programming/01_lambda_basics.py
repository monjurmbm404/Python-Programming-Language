"""
========================================
01_lambda_basics.py
========================================
Lambda Function:

✔ Anonymous (no name) function
✔ Small single-line function
✔ Syntax: lambda arguments: expression
"""

# Normal function
def add(a, b):
    return a + b

print("Normal function:", add(5, 3))

# Lambda function
add_lambda = lambda a, b: a + b

print("Lambda function:", add_lambda(5, 3))