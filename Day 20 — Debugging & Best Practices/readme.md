# 🐍 Python Programming – Day 20: Debugging & Best Practices

---

## 📌 Overview (Beginner Friendly)

In **Day 20**, you will learn one of the most important skills in programming:

👉 **How to find errors and fix them (Debugging)**
👉 **How to write clean and professional code (Best Practices)**

Even expert developers make mistakes — the real skill is **finding and fixing them quickly**.

---

## 💡 Why this topic is important?

✔ Helps you understand errors easily
✔ Saves hours of confusion
✔ Makes your code professional
✔ Required for real-world development & jobs

---

# 📁 01. Traceback Reading

## 📘 What is Traceback?

A **traceback** is Python’s error report.

It tells you:

- What went wrong ❌
- Where it happened 📍
- Which line caused it 📌

---

## 🧠 Example:

```python id="dbg1"
# print(10 / 0)  # This causes error

"""
Traceback shows:
✔ File name
✔ Line number
✔ Error type
✔ Error message
"""

print("Learn how to read errors 🚀")
```

---

# 📁 02. Common Errors in Python

## 📘 Types of Errors:

- SyntaxError → wrong code structure
- NameError → variable not defined
- TypeError → wrong data type
- ValueError → wrong value
- IndexError → invalid index
- KeyError → missing dictionary key

---

## 🧠 Example:

```python id="dbg2"
# print(x)  # NameError
# print("10" + 5)  # TypeError
# int("abc")  # ValueError

arr = [1, 2, 3]
# print(arr[5])  # IndexError

data = {"name": "Python"}
# print(data["age"])  # KeyError

print("Errors explained")
```

---

# 🐞 03. Debugging Techniques

## 📘 What is Debugging?

Debugging means:

👉 Finding and fixing errors in your code

---

## 🧠 Example:

```python id="dbg3"
a = 10
b = 20

print("a:", a)
print("b:", b)

c = a + b

print("Result:", c)
```

---

## 💡 Beginner Tip:

👉 Use `print()` to check values step-by-step

---

# 🧼 04. Clean Code Basics

## 📘 What is Clean Code?

Clean code is:

✔ Easy to read  
✔ Easy to understand  
✔ Easy to maintain

---

## 🧠 Example:

```python id="clean1"
# BAD
x = 10
y = 20
z = x + y
print(z)

# GOOD
num1 = 10
num2 = 20
total_sum = num1 + num2

print("Total Sum:", total_sum)
```

---

## 💡 Rule:

👉 Code is read more than it is written

---

# 🏗 05. Naming Conventions

## 📘 Good Naming Style:

- Variables → snake_case
- Functions → snake_case
- Classes → PascalCase

---

## 🧠 Example:

```python id="name1"
student_name = "Monjur"
total_marks = 95

def calculate_average():
    pass

class StudentData:
    pass
```

---

## 💡 Tip:

👉 Use meaningful names instead of x, y, z

---

# 🔍 06. Debugging Example

## 📘 Step-by-step debugging:

```python id="dbg4"
def divide_numbers(a, b):
    print("Debug a:", a)
    print("Debug b:", b)

    if b == 0:
        print("Error: Cannot divide by zero")
        return None

    result = a / b
    print("Result:", result)

    return result

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
```

---

# 🧠 07. Best Practices Summary

## 📘 Good Developer Habits:

✔ Write simple code  
✔ Use meaningful names  
✔ Break code into functions  
✔ Handle errors properly  
✔ Avoid repeating code  
✔ Keep logic clean

---

## 🧠 Example:

```python id="best1"
print("Debugging & Best Practices Completed 🚀")
```

---

# 🎯 Day 20 Summary

You Learned:

## 🧠 Debugging

✔ Reading traceback  
✔ Finding errors step-by-step

## 🐞 Common Errors

✔ Syntax, Name, Type, Value, Index, Key

## 🧼 Clean Code

✔ Readable and simple code

## 🏗 Best Practices

✔ Professional coding habits

---

# 🚀 YOU ARE NOW HERE:

## 🎉 Python Journey: Day 01 → Day 20 Completed

You now understand:

✔ Python basics  
✔ Functions  
✔ OOP basics (coming next)  
✔ File handling  
✔ Modules  
✔ Debugging

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
