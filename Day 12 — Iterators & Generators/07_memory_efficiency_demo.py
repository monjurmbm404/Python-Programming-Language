"""
========================================
07_memory_efficiency_demo.py
========================================
Why Generators are useful:

✔ Save memory
✔ Generate values on the fly
"""

# Large range using generator
def large_range(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = large_range(1000000)

# Only prints first 5 values (not storing all in memory)
for _ in range(5):
    print(next(gen))