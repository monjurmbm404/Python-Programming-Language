"""
========================================
03_builtin_modules.py
========================================
Built-in Modules:

✔ math   → mathematical functions
✔ random → random numbers
"""

import math
import random

# Math module
print("Ceil:", math.ceil(4.3))
print("Floor:", math.floor(4.9))

# Random module
print("Random number (0-1):", random.random())
print("Random int (1-10):", random.randint(1, 10))

# Random choice
colors = ["red", "green", "blue"]
print("Random color:", random.choice(colors))