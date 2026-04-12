"""
========================================
02_iter_next_function.py
========================================
iter() and next():

✔ iter() → creates iterator
✔ next() → gets next value
"""

text = "Python"

it = iter(text)

print(next(it))  # P
print(next(it))  # y
print(next(it))  # t
print(next(it))  # h
print(next(it))  # o
print(next(it))  # n