"""
========================================
02_star_patterns.py
========================================
Star Patterns:

✔ Most common pattern practice
"""

# Pattern 1: Square
# * * *
# * * *
# * * *

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

print()

# Pattern 2: Right Triangle
# *
# * *
# * * *

for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()