# 🐍 Python Programming – Day 18: Standard Library Essentials

---

## 📌 Overview (Beginner Friendly)

In Python, a **library** is a collection of ready-made code.

👉 You don’t need to write everything from scratch
👉 Python already gives you powerful tools called **Standard Library**

---

## 💡 What is Standard Library?

The **Python Standard Library** is a set of built-in modules that help you do common tasks like:

- Math calculations 🧮
- Random number generation 🎲
- Date & time handling 📅
- File & folder management 🗂

👉 You just **import and use them**

---

# 🧮 01. math Module

## 📁 01_math_module.py

### 📘 Beginner Explanation:

The `math` module helps you do **mathematical calculations easily**.

Instead of writing formulas yourself, Python gives ready functions.

---

### 🧠 Example:

```python id="math1"
import math

print("Square root:", math.sqrt(25))   # √25
print("Power:", math.pow(2, 3))        # 2³

print("Ceil:", math.ceil(4.2))         # round up
print("Floor:", math.floor(4.8))       # round down

print("Pi:", math.pi)                  # 3.14159...
print("Factorial:", math.factorial(5)) # 5 × 4 × 3 × 2 × 1
```

---

# 🎲 02. random Module

## 📁 02_random_module.py

### 📘 Beginner Explanation:

The `random` module is used when you want **random results**, like:

- Games 🎮
- Lottery numbers 🎯
- Random choices

---

### 🧠 Example:

```python id="random1"
import random

print("Random float:", random.random())   # 0 to 1

print("Random number:", random.randint(1, 10))  # 1 to 10

colors = ["red", "green", "blue"]
print("Random color:", random.choice(colors))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled:", numbers)
```

---

# 📅 03. datetime Module

## 📁 03_datetime_module.py

### 📘 Beginner Explanation:

The `datetime` module helps you work with:

- Current date 📅
- Current time ⏰
- Formatting dates

---

### 🧠 Example:

```python id="date1"
import datetime

now = datetime.datetime.now()
print("Current date & time:", now)

today = datetime.date.today()
print("Today:", today)

custom = datetime.date(2026, 4, 12)
print("Custom date:", custom)

print(now.strftime("%Y-%m-%d %H:%M:%S"))
```

---

# 🗂 04. os Module

## 📁 04_os_module.py

### 📘 Beginner Explanation:

The `os` module helps you control your **computer system using Python**.

You can:

- See files 📂
- Create folders 📁
- Check directories

---

### 🧠 Example:

```python id="os1"
import os

print("Current folder:", os.getcwd())

print("Files in folder:", os.listdir())

if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
    print("Folder created")
```

---

# 📁 05. File Operations using os

## 📁 05_file_operations_with_os.py

### 📘 Beginner Explanation:

This helps you:

- Check if file exists
- Rename files
- Delete files

---

### 🧠 Example:

```python id="fileos1"
import os

file_name = "sample.txt"

if os.path.exists(file_name):
    print("File exists")

with open(file_name, "w") as f:
    f.write("Hello Python")

os.rename(file_name, "renamed_sample.txt")

# os.remove("renamed_sample.txt")  # delete file
```

---

# 📊 06. Real Practical Example

## 📁 06_practical_combination.py

### 📘 Beginner Explanation:

Here we combine multiple modules together:

- random → marks
- math → calculations
- datetime → time info

---

### 🧠 Example:

```python id="combo1"
import math
import random
import datetime

marks = [random.randint(50, 100) for _ in range(5)]

print("Marks:", marks)

avg = sum(marks) / len(marks)
print("Average:", round(avg, 2))

print("Generated on:", datetime.datetime.now())

print("Square root of average:", math.sqrt(avg))
```

---

# ⚡ 07. Summary

## 📘 What you learned today:

### 🧮 math module

✔ Calculations (sqrt, power, factorial)

### 🎲 random module

✔ Random numbers & choices

### 📅 datetime module

✔ Date and time handling

### 🗂 os module

✔ File & folder management

---

# 🚀 Final Beginner Understanding

👉 These modules are like **tools in a toolbox**

Instead of building everything yourself:

✔ Python already gives you tools  
✔ You just learn how to use them

---

# 🚀 What’s Next?

👉 **Day 19 — Command Line & Environment**

You will learn:

- `sys.argv`
- Basic CLI Programs
- Virtual Environment (`venv`)
- Why environments matter

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
