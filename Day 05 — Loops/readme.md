# 🐍 Python Programming – Day 05: Loops

---

## 📌 Overview

In this chapter, you will learn about **Loops in Python**.

Loops are used to **repeat a block of code multiple times** without writing it again and again.

They are very important for:

- Repeating tasks 🔁
- Processing data 📊
- Pattern building ⭐
- Automation 🤖

---

# 🔁 01. for Loop

## 📁 01_for_loop.py

### 📘 What you learn:

- Used to iterate over sequences (range, string, list, etc.)

### 🧠 Example:

```python id="pyfor1"
for i in range(1, 6):
    print("Number:", i)

text = "Python"

for char in text:
    print(char)
```

---

# 🔁 02. while Loop

## 📁 02_while_loop.py

### 📘 What you learn:

- Runs as long as condition is True
- Must update variable to avoid infinite loop

### 🧠 Example:

```python id="pywhile1"
i = 1

while i <= 5:
    print("Value:", i)
    i += 1
```

---

# 🔁 03. Nested Loops

## 📁 03_nested_loops.py

### 📘 What you learn:

- Loop inside another loop
- Used for patterns and grids

### 🧠 Example:

```python id="pynested1"
for i in range(1, 4):
    for j in range(1, 4):
        print("*", end=" ")
    print()
```

---

# ⛔ 04. break Statement

## 📁 04_break_statement.py

### 📘 What you learn:

- Stops loop immediately

### 🧠 Example:

```python id="pybreak1"
for i in range(1, 10):
    if i == 5:
        print("Loop stopped at", i)
        break
    print(i)
```

---

# ⏭ 05. continue Statement

## 📁 05_continue_statement.py

### 📘 What you learn:

- Skips current iteration

### 🧠 Example:

```python id="pycont1"
for i in range(1, 6):
    if i == 3:
        print("Skipped:", i)
        continue
    print("Value:", i)
```

---

# 🧩 06. pass Statement

## 📁 06_pass_statement.py

### 📘 What you learn:

- Does nothing (placeholder)
- Used when code is required syntactically

### 🧠 Example:

```python id="pypass1"
for i in range(1, 5):
    if i == 3:
        pass
    print("Number:", i)
```

---

# 🎯 Day 05 Summary

After completing this day, you learned:

✅ for Loop  
✅ while Loop  
✅ Nested Loops  
✅ break Statement  
✅ continue Statement  
✅ pass Statement

---

## 🚀 What’s Next?

Next step:
👉 **Day 06 — Pattern & Logic Building**

You’ll learn:

- Number Patterns
- Tuple
- Pyramid Patterns
- Reverse Patterns
- Loop-based Logic

---

> 💡 **Pro Tip:** Practice loops by building:
>
> - Multiplication table
> - Number patterns
> - Sum of numbers
> - Even/Odd counter

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


