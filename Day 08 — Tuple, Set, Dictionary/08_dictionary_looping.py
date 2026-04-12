"""
========================================
08_dictionary_looping.py
========================================
Looping Dictionary:

✔ Loop keys, values, or both
"""

student = {
    "name": "Monjur",
    "age": 22,
    "course": "Python"
}

# Keys
for key in student:
    print("Key:", key)

print()

# Values
for value in student.values():
    print("Value:", value)

print()

# Key + Value
for key, value in student.items():
    print(key, ":", value)