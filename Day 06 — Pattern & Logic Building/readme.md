# 🐍 Python Programming – Day 06: Pattern & Logic Building

---

## 📌 Overview

In this chapter, you will learn how to build **patterns and logic using loops**.

Pattern problems are very important because they:

- Improve your logic thinking 🧠
- Strengthen nested loop concepts 🔁
- Prepare you for coding interviews 💼
- Build problem-solving confidence 🚀

---

# 🔢 01. Number Patterns

## 📁 01_number_patterns.py

### 📘 What you learn:

- Printing numbers using nested loops
- Row-column logic

### 🧠 Example:

```python id="py6n1"
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()

print()

for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

---

# ⭐ 02. Star Patterns

## 📁 02_star_patterns.py

### 📘 What you learn:

- Printing stars in different shapes
- Square and triangle patterns

### 🧠 Example:

```python id="py6s1"
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

print()

for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()
```

---

# 🔺 03. Pyramid Patterns

## 📁 03_pyramid_patterns.py

### 📘 What you learn:

- Space handling in loops
- Pyramid structure logic

### 🧠 Example:

```python id="py6p1"
rows = 4

for i in range(1, rows + 1):

    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()
```

---

# 🔄 04. Reverse Patterns

## 📁 04_reverse_patterns.py

### 📘 What you learn:

- Reverse iteration using loops
- Decreasing patterns

### 🧠 Example:

```python id="py6r1"
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print()

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

---

# 🧠 05. Loop Logic Building

## 📁 05_loop_logic_building.py

### 📘 What you learn:

- Real-world logic using loops
- Sum, condition, and multiplication logic

### 🧠 Example:

```python id="py6l1"
total = 0

for i in range(1, 6):
    total += i
    print("Number:", i)

print("Sum:", total)

print()

for i in range(1, 11):
    if i % 2 == 0:
        print("Even:", i)

print()

num = 3

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```

---

# 🎯 Day 06 Summary

After completing this day, you learned:

✅ Number Patterns  
✅ Star Patterns  
✅ Pyramid Patterns  
✅ Reverse Patterns  
✅ Loop-based Logic Building

---

## 🚀 What’s Next?

Next step:
👉 **Day 07 — Lists in Python**

You’ll learn:

- List Basics
- Indexing & Slicing
- List Methods
- Looping through lists
- Operations (sum, max, min)
- Searching
- Sorting

---

> 💡 **Pro Tip:**
> Pattern practice = Logic strength 💪
> The more patterns you solve, the better your coding becomes.

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
