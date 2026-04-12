"""
========================================
05_keyword_arguments.py
========================================
Keyword Arguments:

✔ Pass arguments using parameter names
"""

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=22, name="Monjur")  # order doesn't matter