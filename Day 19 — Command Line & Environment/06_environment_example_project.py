"""
========================================
06_environment_example_project.py
========================================
Real Example:

✔ CLI + environment usage idea
"""

import sys

def greet(name):
    return f"Hello {name}, welcome to Python CLI!"

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(greet(name))
else:
    print("Please provide your name:")