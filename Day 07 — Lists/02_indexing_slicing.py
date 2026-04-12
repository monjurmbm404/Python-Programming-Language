"""
========================================
02_indexing_slicing.py
========================================
Indexing & Slicing:

✔ Index starts from 0
✔ Negative indexing allowed
✔ Slicing: list[start:end]
"""

arr = [10, 20, 30, 40, 50]

# Indexing
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing
print("First 3 elements:", arr[0:3])
print("From index 2:", arr[2:])
print("Reverse:", arr[::-1])