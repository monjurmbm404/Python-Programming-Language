"""
========================================
04_generator_basic.py
========================================
Generator Concept:

✔ Generator = function that returns iterator
✔ Uses 'yield' instead of return
✔ Saves memory (lazy execution)
"""

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))