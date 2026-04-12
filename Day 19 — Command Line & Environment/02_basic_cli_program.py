"""
========================================
02_basic_cli_program.py
========================================
Basic CLI Program:

✔ Take input from command line
✔ Perform simple operations
"""

import sys

# Example usage:
# python file.py 10 20

if len(sys.argv) != 3:
    print("Usage: python file.py num1 num2")
    sys.exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)