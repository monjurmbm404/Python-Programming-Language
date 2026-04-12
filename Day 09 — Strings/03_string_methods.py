"""
========================================
03_string_methods.py
========================================
String Methods:

✔ length, upper, lower, strip, replace, find
"""

text = "  Python Programming  "

print("Length:", len(text))
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Strip:", text.strip())  # remove spaces

print("Replace:", text.replace("Python", "Java"))
print("Find:", text.find("Programming"))