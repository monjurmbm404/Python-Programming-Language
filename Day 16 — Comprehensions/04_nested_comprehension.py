"""
========================================
04_nested_comprehension.py
========================================
Nested Comprehension:

✔ Comprehension inside comprehension
✔ Used for matrices and complex structures
"""

# 3x3 matrix using nested loop
matrix = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(i * j)
    matrix.append(row)

print("Normal matrix:", matrix)

# Nested list comprehension
matrix2 = [[i * j for j in range(3)] for i in range(3)]

print("Nested comprehension matrix:", matrix2)