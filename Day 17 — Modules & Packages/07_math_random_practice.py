"""
========================================
07_math_random_practice.py
========================================
Practice with math + random
"""

import math
import random

# Random exam marks
marks = [random.randint(40, 100) for _ in range(5)]

print("Marks:", marks)
print("Max:", max(marks))
print("Min:", min(marks))
print("Average:", sum(marks) / len(marks))

# Round example
print("Rounded sqrt of 50:", round(math.sqrt(50), 2))