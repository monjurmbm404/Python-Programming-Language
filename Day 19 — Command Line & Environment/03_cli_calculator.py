"""
========================================
03_cli_calculator.py
========================================
CLI Calculator:

✔ Real-world CLI example
"""

import sys

# Example:
# python file.py 10 + 5

if len(sys.argv) != 4:
    print("Usage: python file.py num1 operator num2")
    sys.exit()

num1 = int(sys.argv[1])
op = sys.argv[2]
num2 = int(sys.argv[3])

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid operator")