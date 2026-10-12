# 🐍 Python Programming – Day 08: Tuple, Set, Dictionary

---

## 📌 Overview

In this chapter, you will learn **three important data structures in Python**:

- 📦 Tuple (Immutable Collection)
- 🧩 Set (Unique Collection)
- 🗂 Dictionary (Key-Value Collection)

These are widely used in real-world programming, especially in data handling and problem solving.

---

# 📦 PART 1 — TUPLE

---

## 📌 What is a Tuple?

A **tuple** is an ordered collection of values.

### 💡 Key Features:

- ✔ Ordered (keeps index)
- ✔ Immutable (cannot be changed)
- ✔ Allows duplicates
- ✔ Uses `()` brackets

---

## 📁 01_tuple_basics.py

```python id="py8b1"
"""
Tuple Basics:

✔ Ordered collection
✔ Immutable (cannot change values)
"""

numbers = (10, 20, 30, 40)

print("Tuple:", numbers)
print("Type:", type(numbers))
```

---

## 📁 02_tuple_immutable.py

```python id="py8b2"
"""
Tuple Immutability:

✔ You cannot change values after creation
"""

t = (1, 2, 3)

# t[0] = 100  ❌ Not allowed

print("Tuple:", t)
```

---

## 📁 03_tuple_packing_unpacking.py

```python id="py8b3"
"""
Packing & Unpacking:

✔ Packing = storing multiple values in one tuple
✔ Unpacking = extracting values into variables
"""

person = ("Monjur", 22, "Developer")

name, age, job = person

print(name)
print(age)
print(job)
```

---

# 🧩 PART 2 — SET

---

## 📌 What is a Set?

A **set** is an unordered collection of unique values.

### 💡 Key Features:

- ✔ No duplicate values
- ✔ Unordered
- ✔ Mutable
- ✔ Uses `{}` brackets

---

## 📁 04_set_basics.py

```python id="py8b4"
"""
Set Basics:

✔ Stores only unique values
✔ Removes duplicates automatically
"""

numbers = {1, 2, 3, 3, 4, 5}

print("Set:", numbers)
```

---

## 📁 05_set_operations.py

```python id="py8b5"
"""
Set Operations:

✔ Union (|)
✔ Intersection (&)
✔ Difference (-)
"""

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference A-B:", a - b)
print("Difference B-A:", b - a)
```

---

# 🗂 PART 3 — DICTIONARY

---

## 📌 What is a Dictionary?

A **dictionary** stores data in **key-value pairs**.

### 💡 Key Features:

- ✔ Fast lookup
- ✔ Uses key-value structure
- ✔ Mutable (can change values)
- ✔ Uses `{}` with keys

---

## 📁 06_dictionary_basics.py

```python id="py8b6"
"""
Dictionary Basics:

✔ Key-value pairs
"""

student = {
    "name": "Monjur",
    "age": 22,
    "course": "Python"
}

print(student)
```

---

## 📁 07_dictionary_access_update_delete.py

```python id="py8b7"
"""
Access, Update, Delete Dictionary:

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

print(student)
```

---

## 📁 08_dictionary_looping.py

```python id="py8b8"
"""
Looping Dictionary:

✔ Loop through keys, values, or both
"""

student = {
    "name": "Monjur",
    "age": 22,
    "course": "Python"
}

# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Key + Value
for key, value in student.items():
    print(key, ":", value)
```

---

# 🎯 Day 08 Summary

After completing this lesson, you learned:

## 📦 Tuple

- Ordered collection
- Immutable (cannot change)
- Packing & unpacking

## 🧩 Set

- Stores unique values only
- Supports mathematical operations
- Fast and efficient

## 🗂 Dictionary

- Key-value data structure
- Fast data access
- Used in real-world applications

---

# 🚀 What’s Next?

👉 **Day 09 — Strings in Python**

You will learn:

- String Basics
- Indexing & Slicing
- String Methods
- Formatting (f-string)
- Reverse String
- Palindrome Check

---




# Author

## **Engr. Md Monjur Bakth Mazumder**

🎓 **Secondary School Certificate (SSC) from [Shah Helal High School](https://www.shahhelalhs.edu.bd/)**

🎓 **Diploma in Computer Science and Technology from [Moulvibazar Polytechnic Institute (MPI)](https://mpi.moulvibazar.gov.bd/)**

🎓 **BSc in Computer Science & Engineering (CSE)** _(Ongoing)_ **at [Sylhet International University (SIU)](https://siu.edu.bd/)**

---

## Support the Project

If you found this repository helpful, please consider giving it a **⭐ Star**. It helps others discover the project and motivates future development.

---


## Connect with Me

### Professional Profiles

| Platform | Link |
|:---|:---|
| Portfolio | [monjurmbm404.github.io](https://monjurmbm404.github.io) |
| GitHub | [monjurmbm404](https://github.com/monjurmbm404) |
| LinkedIn | [monjurmbm404](https://www.linkedin.com/in/monjurmbm404) |
| Medium | [@monjurmbm404](https://medium.com/@monjurmbm404) |

### Competitive Programming

| Platform | Link |
|:---|:---|
| Codeforces | [monjurmbm404](https://codeforces.com/profile/monjurmbm404) |
| CodeChef | [monjurmbm404](https://www.codechef.com/users/monjurmbm404) |
| LeetCode | [monjurmbm404](https://leetcode.com/u/monjurmbm404) |
| VJudge | [monjurmbm404](https://vjudge.net/user/monjurmbm404) |

### Social Media

| Platform | Link |
|:---|:---|
| Facebook | [monjurmbm404](https://www.facebook.com/monjurmbm404) |
| X (Twitter) | [@monjurmbm404](https://x.com/monjurmbm404) |
| YouTube | [@monjurmbm404](https://youtube.com/@monjurmbm404) |

### Contact Information

| Type | Email |
|:---|:---|
| Professional | [monjurmbm404@gmail.com](mailto:monjurmbm404@gmail.com) |


