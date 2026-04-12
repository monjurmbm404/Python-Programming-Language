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

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
