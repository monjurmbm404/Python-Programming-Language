"""
========================================
01_number_patterns.py
========================================
Number Patterns:

✔ Using nested loops to print numbers
✔ Helps build logic thinking
"""

# Pattern 1:
# 1 2 3
# 1 2 3
# 1 2 3

for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()

print()

# Pattern 2:
# 1
# 1 2
# 1 2 3

for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()