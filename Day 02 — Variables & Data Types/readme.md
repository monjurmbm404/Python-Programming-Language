# 🐍 Python Programming – Day 02: Variables & Data Types

Welcome to **Day 02 of Python Learning Series**! 🎉
Today you’ll learn how Python **stores data**, how variables work, and how to **identify and convert data types**.

This is one of the most important foundations of programming — so take your time and practice! 🚀

---

## 🧩 What You’ll Learn Today

- Variables & Dynamic Typing
- Variable Naming Rules
- Basic Data Types (`int`, `float`, `str`, `bool`)
- Type Checking using `type()`
- Type Conversion (`int()`, `float()`, `str()`, `bool()`)

---

## 📦 1. Variables & Dynamic Typing

A **variable** is like a container that stores data.

In Python:

- You **don’t need to declare the type**
- Python automatically detects it → this is called **dynamic typing**

```python
x = 10          # int
y = 3.14        # float
name = "Monjur" # string
is_active = True # boolean
```

💡 You can even change the type later:

```python
x = "Now I am a string"
```

👉 Same variable, different type — very powerful!

---

## 🧾 2. Variable Naming Rules

Follow these rules when naming variables:

✅ Use letters, numbers, underscore `_`  
✅ Must start with a letter or `_`  
❌ Cannot start with a number  
❌ Cannot use keywords (`if`, `for`, `class`, etc.)  
✅ Case-sensitive (`age` ≠ `Age`)

```python
name = "Python"      # ✅ valid
_age = 22            # ✅ valid
total_score = 100    # ✅ valid

# 2name = "error"    ❌ invalid
# class = "error"    ❌ invalid
```

💡 Tip: Use meaningful names like `student_age` instead of `a`.

---

## 🔢 3. Basic Data Types

Python has several built-in data types:

| Type    | Example    | Description     |
| ------- | ---------- | --------------- |
| `int`   | 10         | Whole numbers   |
| `float` | 3.14       | Decimal numbers |
| `str`   | "Hello"    | Text (string)   |
| `bool`  | True/False | Boolean values  |

```python
a = 10
b = 3.14
c = "Hello"
d = True
```

---

## 🔍 4. Type Checking

Use `type()` to check the data type of a variable:

```python
x = 10
print(type(x))  # <class 'int'>
```

More examples:

```python
print(type(3.14))   # float
print(type("Hi"))   # str
print(type(False))  # bool
```

---

## 🔄 5. Type Conversion

Sometimes you need to convert one data type to another.

### Common functions:

- `int()` → convert to integer
- `float()` → convert to decimal
- `str()` → convert to string
- `bool()` → convert to boolean

---

### 🔹 Examples

```python
# String to int
a = "10"
b = int(a)

# int to float
x = 5
y = float(x)

# float to int
p = 3.99
q = int(p)  # becomes 3

# int to string
num = 100
text = str(num)
```

---

### 🔹 Boolean Conversion

```python
print(bool(0))     # False
print(bool(1))     # True
print(bool(""))    # False
print(bool("Hi"))  # True
```

💡 Rule:

- `0`, `""`, `None` → **False**
- Everything else → **True**

---

## ✅ Day 02 Summary

Today you learned:

✅ Variables & Dynamic Typing  
✅ Variable Naming Rules  
✅ Data Types: `int`, `float`, `str`, `bool`  
✅ Type Checking using `type()`  
✅ Type Conversion (`int()`, `float()`, `str()`, `bool()`)

---

## 🚀 What’s Next?

Next step:
👉 **Day 03 — Operators in Python**

You’ll learn:

- Arithmetic Operators
- Assignment Operators
- Relational Operators
- Logical Operators
- Membership Operators
- Identity Operators
- Bitwise Operators
- Ternary Operator

---

> 💡 **Pro Tip:** Practice by creating your own variables and converting between types. Try combining numbers and strings to see how Python behaves!

---


# Author

## **Engr. Md Monjur Bakth Mazumder**

🎓 **Secondary School Certificate (SSC) from [Shah Helal High School](https://www.shahhelalhs.edu.bd/)**

🎓 **Diploma in Computer Science and Technology from [Moulvibazar Polytechnic Institute (MPI)](https://mpi.moulvibazar.gov.bd/)**

🎓 **BSc in Computer Science & Engineering (CSE)** _(Ongoing)_ **at [Sylhet International University (SIU)](https://siu.edu.bd/)**

📧 **Email:** monjurmbm404@gmail.com

---

## ⭐ Support the Project

If you found this repository helpful, please consider giving it a **⭐ Star**. It helps others discover the project and motivates future development.

---

## 🌐 Connect with Me

| Platform       | Link                                        |
| -------------- | ------------------------------------------- |
| 💻 GitHub      | https://github.com/monjurmbm404             |
| 💼 LinkedIn    | https://linkedin.com/in/monjurmbm404        |
| 🧩 LeetCode    | https://leetcode.com/u/monjurmbm404         |
| ⚔️ Codeforces  | https://codeforces.com/profile/monjurmbm404 |
| 🍽️ CodeChef    | https://www.codechef.com/users/monjurmbm404 |
| 🏆 VJudge      | https://vjudge.net/user/monjurmbm404        |
| 📘 Facebook    | https://www.facebook.com/monjurmbm404       |
| 🐦 X (Twitter) | https://x.com/monjurmbm404                  |
| ▶️ YouTube     | https://youtube.com/@monjurmbm404           |
| ✍️ Medium      | https://medium.com/@monjurmbm404            |

