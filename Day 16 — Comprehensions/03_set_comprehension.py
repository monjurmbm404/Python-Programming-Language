"""
========================================
03_set_comprehension.py
========================================
Set Comprehension:

✔ Creates unique elements automatically
"""

# Normal set
nums = set()
for i in range(1, 6):
    nums.add(i * 2)

print("Normal set:", nums)

# Set comprehension
nums2 = {i * 2 for i in range(1, 6)}

print("Set comprehension:", nums2)

# Unique squares
unique = {i * i for i in range(1, 6)}
print("Unique squares:", unique)