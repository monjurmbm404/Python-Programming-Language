"""
========================================
05_generator_with_loop.py
========================================
Generator with Loop:

✔ Produces values one by one
"""

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(5)

for value in gen:
    print(value)