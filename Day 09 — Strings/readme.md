# 🐍 Python Programming – Day 09: Strings

---

## 📌 Overview

In this chapter, you will learn about **Strings in Python**, one of the most commonly used data types.

A **string** is a sequence of characters used to store text.

---

## 💡 Key Features of Strings:

- ✔ Sequence of characters
- ✔ Can use single `' '` or double `" "` quotes
- ✔ Immutable (cannot change original string)
- ✔ Supports indexing & slicing
- ✔ Has many built-in methods

---

# 🔤 PART 1 — STRING BASICS

---

## 📁 01_string_basics.py

```python id="py9b1"
"""
String Basics:

✔ Strings store text data
✔ Can use ' ' or " "
✔ Immutable type
"""

name = "Python"
message = 'Hello World'

print(name)
print(message)
print(type(name))
```

---

# 📍 PART 2 — INDEXING & SLICING

---

## 📌 What is Indexing?

Each character has a position starting from **0**.

```
P  y  t  h  o  n
0  1  2  3  4  5
```

---

## 📁 02_indexing_slicing.py

```python id="py9b2"
"""
Indexing & Slicing:

✔ Access characters using index
✔ Slice part of string
"""

text = "Python"

print(text[0])    # P
print(text[-1])   # n

print(text[0:4])   # Pyth
print(text[2:])    # thon
print(text[::-1])  # reverse string
```

---

# 🧰 PART 3 — STRING METHODS

---

## 📁 03_string_methods.py

```python id="py9b3"
"""
String Methods:

✔ Built-in functions for strings
"""

text = "  Python Programming  "

print(len(text))
print(text.upper())
print(text.lower())
print(text.strip())   # remove spaces
print(text.replace("Python", "Java"))
print(text.find("Programming"))
```

---

# 🎯 PART 4 — FORMATTING STRINGS

---

## 📁 04_f_string_formatting.py

```python id="py9b4"
"""
f-string Formatting:

✔ Used for clean and fast output
"""

name = "Monjur"
age = 22

print(f"My name is {name} and I am {age} years old.")
print(f"Next year age: {age + 1}")
```

---

# 🔁 PART 5 — STRING LOGIC

---

## 📁 05_reverse_string.py

```python id="py9b5"
"""
Reverse String:

✔ Using slicing technique
"""

text = "Python"

print(text[::-1])
```

---

## 📁 06_palindrome_check.py

```python id="py9b6"
"""
Palindrome Check:

✔ Same forward and backward string
"""

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

---

# 🎯 DAY 09 SUMMARY

After completing this chapter, you learned:

## 🔤 Strings Basics

- Creating strings
- Data type of string

## 📍 Indexing & Slicing

- Access characters
- Reverse strings

## 🧰 String Methods

- len(), upper(), lower(), strip()
- replace(), find()

## 🎯 Formatting

- f-string usage

## 🔁 Problem Solving

- Reverse string
- Palindrome check

---

# 🚀 What’s Next?

👉 **Day 10 — Functions in Python**

You will learn:

- Function Definition
- Parameters & Arguments
- Return Values
- Default Arguments
- Keyword Arguments
- Variable Scope

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


