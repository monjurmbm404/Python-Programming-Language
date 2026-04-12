"""
========================================
06_identity_operators.py
========================================
Identity Operators:

is     -> same object in memory
is not -> different object
"""

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)      # False (different objects)
print(a is c)      # True  (same object)
print(a is not b)  # True