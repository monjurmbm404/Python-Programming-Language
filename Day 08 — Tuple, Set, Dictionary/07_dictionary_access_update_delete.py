"""
========================================
07_dictionary_access_update_delete.py
========================================
Access, Update, Delete:

✔ Access values using keys
"""

student = {
    "name": "Monjur",
    "age": 22,
    "city": "Sylhet"
}

# Access
print(student["name"])

# Update
student["age"] = 23

# Add new key
student["job"] = "Developer"

# Delete key
del student["city"]

print("Updated Dictionary:", student)