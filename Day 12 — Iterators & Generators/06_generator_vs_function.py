"""
========================================
06_generator_vs_function.py
========================================
Generator vs Normal Function:

✔ return → stops function
✔ yield → pauses function (remembers state)
"""

# Normal function
def normal_function():
    return [1, 2, 3]

# Generator function
def generator_function():
    yield 1
    yield 2
    yield 3

print("Normal function:", normal_function())

gen = generator_function()

print("Generator output:")
for i in gen:
    print(i)