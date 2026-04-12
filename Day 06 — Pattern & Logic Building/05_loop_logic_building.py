"""
========================================
05_loop_logic_building.py
========================================
Loop-based Logic Building:

✔ Helps in solving coding problems
"""

# Example 1: Print numbers with sum
total = 0

for i in range(1, 6):
    total += i
    print("Number:", i)

print("Sum:", total)

print()

# Example 2: Print even numbers only
for i in range(1, 11):
    if i % 2 == 0:
        print("Even:", i)

print()

# Example 3: Multiplication table
num = 3

for i in range(1, 11):
    print(num, "x", i, "=", num * i)