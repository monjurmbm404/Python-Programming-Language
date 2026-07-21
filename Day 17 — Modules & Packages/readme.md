# 🐍 Python Programming – Day 17: Modules & Packages

---

## 📌 Overview

In **Day 17**, you will learn how to organize and reuse code using:

# 📦 Modules & Packages

These are very important for writing **clean, reusable, and professional Python code**.

---

## 💡 Why Modules & Packages are Important?

✔ Avoid rewriting code again and again  
✔ Organize large projects properly  
✔ Reuse built-in and custom functions  
✔ Used in all real-world Python projects  
✔ Essential for backend & software development

---

# 📁 01. Import Basics

## 📄 01_import_basics.py

### 📘 What you learn:

- Importing built-in modules
- Using module functions

### 🧠 Example:

```python id="py17b1"
import math

print(math.sqrt(16))
print(math.pi)
```

---

# 📁 02. From Import

## 📄 02_from_import.py

### 📘 What you learn:

- Import specific functions only

### 🧠 Example:

```python id="py17b2"
from math import sqrt, pow

print(sqrt(25))
print(pow(2, 3))
```

---

# 📁 03. Built-in Modules

## 📄 03_builtin_modules.py

### 📘 What you learn:

- Using math and random modules

### 🧠 Example:

```python id="py17b3"
import math
import random

print(math.ceil(4.3))
print(math.floor(4.9))

print(random.randint(1, 10))
print(random.choice(["red", "green", "blue"]))
```

---

# 📁 04. Custom Module Usage

## 📄 04_custom_module.py

### 📘 What you learn:

- Import your own Python file as module

### 🧠 Example:

```python id="py17b4"
import mymodule

print(mymodule.greet("Monjur"))
```

---

# 📁 05. Creating Custom Module

## 📄 05_create_custom_module_file.py

### 📘 What you learn:

- How to create your own module file

### 🧠 Example:

```python id="py17b5"
def greet(name):
    return "Hello " + name

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

---

# 📁 06. Package Basics

## 📄 06_package_basics.py

### 📘 What you learn:

- What is a package
- Folder-based modules

### 🧠 Example:

```python id="py17b6"
print("Package concept explained (structure only)")
```

---

# 📁 07. Practice Example

## 📄 07_math_random_practice.py

### 📘 What you learn:

- Real usage of math + random together

### 🧠 Example:

```python id="py17b7"
import math
import random

marks = [random.randint(40, 100) for _ in range(5)]

print(marks)
print(max(marks))
print(min(marks))
print(sum(marks) / len(marks))

print(round(math.sqrt(50), 2))
```

---

# 📁 08. Summary

## 📄 08_modules_summary.py

### 🧠 Example:

```python id="py17b8"
print("Modules & Packages Completed 🚀")
```

---

# 🎯 Day 17 Summary

You Learned:

## 📦 Modules

✔ import full module  
✔ from ... import specific functions

## 🧮 Built-in Modules

✔ math → calculations  
✔ random → randomness

## 🧱 Custom Modules

✔ Create your own reusable Python file

## 📁 Packages

✔ Folder of multiple modules  
✔ Organize large projects

---

# 🚀 What’s Next?

👉 **Day 18 — Standard Library Essentials**

You will learn:

- `math`
- `random`
- `datetime`
- `os` (basic file/folder operations)

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

