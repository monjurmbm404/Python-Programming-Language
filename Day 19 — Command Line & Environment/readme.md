# 🐍 Python Programming – Day 19: Command Line & Environment

---

## 📌 Overview (Beginner Friendly)

In **Day 19**, you will learn how to run Python programs from the **terminal (command line)** and how to manage your Python projects using a **virtual environment**.

These are very important skills for **real-world Python development**.

---

## 💡 Why this topic is important?

✔ Run Python programs like real applications  
✔ Pass input directly from terminal  
✔ Build CLI (Command Line Interface) tools  
✔ Manage project dependencies safely  
✔ Work like a professional developer

---

# 📁 01. sys.argv (Command Line Arguments)

## 📘 What is it?

`sys.argv` allows you to pass data to Python **from the terminal**.

👉 It is a list  
👉 `argv[0]` = file name  
👉 `argv[1]`, `argv[2]` = user inputs

---

## 🧠 Example:

```python id="cli1"
import sys

print("Script Name:", sys.argv[0])

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        print("Argument:", sys.argv[i])
else:
    print("No arguments provided")
```

---

# 📁 02. Basic CLI Program

## 📘 What you learn:

- Taking numbers from terminal
- Performing calculations

---

## 🧠 Example:

```python id="cli2"
import sys

if len(sys.argv) != 3:
    print("Usage: python file.py num1 num2")
    sys.exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
```

---

# 📁 03. CLI Calculator

## 📘 What you learn:

- Real CLI application
- Operator-based calculation

---

## 🧠 Example:

```python id="cli3"
import sys

if len(sys.argv) != 4:
    print("Usage: python file.py num1 operator num2")
    sys.exit()

num1 = int(sys.argv[1])
op = sys.argv[2]
num2 = int(sys.argv[3])

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
```

---

# 🧪 04. Virtual Environment (venv)

## 📘 What is it?

A **virtual environment** is a separate Python space for each project.

👉 Without venv:

- All projects share same packages ❌
- Version conflicts happen ❌

👉 With venv:

- Each project is isolated ✅
- Safe and clean development ✅

---

## 🧠 Explanation:

```python id="venv1"
"""
Virtual Environment Concept:

✔ Isolated Python environment
✔ Prevents dependency conflicts
✔ Used in real projects
"""

print("venv concept explained")
```

---

# ⚙️ 05. venv Commands (IMPORTANT)

## 📘 These are NOT Python code (Terminal commands)

---

```text
# Create virtual environment
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Mac/Linux)
source myenv/bin/activate

# Install package
pip install requests

# List packages
pip list

# Deactivate
deactivate
```

---

# 📁 06. Real CLI Example

## 📘 What you learn:

- Combine CLI + function
- Simple real-world program

---

## 🧠 Example:

```python id="cli4"
import sys

def greet(name):
    return f"Hello {name}, welcome to Python CLI!"

if len(sys.argv) > 1:
    print(greet(sys.argv[1]))
else:
    print("Please provide your name")
```

---

# ⚡ 07. Summary

## 📘 What you learned today:

### 💻 sys.argv

✔ Get input from terminal

### ⚙ CLI Programs

✔ Build command-line tools

### 🧪 Virtual Environment

✔ Isolated project setup

### 📦 pip

✔ Install Python packages

---

# 🚀 Final Beginner Understanding

👉 Today you learned how real Python applications work:

✔ Not just scripts  
✔ But terminal-based tools  
✔ And professional project setup

---

# 🚀 What’s Next?

👉 **Day 20 — Debugging & Best Practices**

You will learn:

- Reading Errors (Traceback)
- Common Errors
- Debugging Techniques
- Clean Code Basics
- Code Structure & Naming

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


