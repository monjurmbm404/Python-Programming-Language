"""
========================================
04_reverse_patterns.py
========================================
Reverse Patterns:

✔ Printing patterns in reverse order
"""

# Reverse star triangle
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print()

# Reverse number pattern
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()