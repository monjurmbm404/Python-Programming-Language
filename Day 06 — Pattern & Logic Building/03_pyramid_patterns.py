"""
========================================
03_pyramid_patterns.py
========================================
Pyramid Patterns:

✔ Important for interview logic building
"""

rows = 4

for i in range(1, rows + 1):

    # spaces
    for j in range(rows - i):
        print(" ", end="")

    # stars
    for k in range(2 * i - 1):
        print("*", end="")

    print()

# Output:
#    *
#   ***
#  *****
# *******