"""
========================================
02_random_module.py
========================================
random Module:

✔ Used for generating random values
✔ Useful in games, simulations
"""

import random

# Random float (0 to 1)
print("Random float:", random.random())

# Random integer
print("Random int (1-10):", random.randint(1, 10))

# Random range
print("Random range:", random.randrange(1, 20, 2))

# Random choice from list
colors = ["red", "green", "blue"]
print("Random color:", random.choice(colors))

# Shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled:", numbers)