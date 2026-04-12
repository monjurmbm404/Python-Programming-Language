"""
========================================
04_default_arguments.py
========================================
Default Arguments:

✔ If no value is passed, default is used
"""

def greet(name="User"):
    print("Hello", name)

greet("Monjur")  # custom value
greet()          # default value