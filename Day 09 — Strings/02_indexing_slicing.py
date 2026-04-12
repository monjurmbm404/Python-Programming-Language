"""
========================================
02_indexing_slicing.py
========================================
Indexing & Slicing:

✔ Index starts from 0
✔ Negative indexing allowed
✔ Slicing: [start:end]
"""

text = "Python"

# Indexing
print(text[0])   # P
print(text[-1])  # n

# Slicing
print(text[0:4])  # Pyth
print(text[2:])   # thon
print(text[::-1]) # reverse