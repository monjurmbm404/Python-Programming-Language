"""
========================================
06_practical_combination.py
========================================
Practical Example:

✔ Using math + random + datetime
"""

import math
import random
import datetime

# Random marks for student
marks = [random.randint(50, 100) for _ in range(5)]

print("Marks:", marks)

# Calculate average
avg = sum(marks) / len(marks)
print("Average:", round(avg, 2))

# Current date
print("Generated on:", datetime.datetime.now())

# Square root of average
print("Sqrt of average:", math.sqrt(avg))