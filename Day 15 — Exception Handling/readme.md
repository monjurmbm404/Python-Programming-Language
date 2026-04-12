# 🐍 Python Programming – Day 15: Exception Handling

---

## 📌 Overview

In **Day 15**, you will learn how to handle **errors safely in Python**.

Sometimes your program crashes because of unexpected problems. Exception handling helps you:

- 🚨 Prevent program crashes
- 🛡 Handle errors gracefully
- 🔄 Keep program running smoothly
- ⚙ Improve user experience

---

## 💡 Why Exception Handling is Important?

✔ Prevents program from stopping unexpectedly  
✔ Used in real-world applications  
✔ Essential for production-level code  
✔ Helps debug and control errors

---

# 📁 01. Errors vs Exceptions

## 📄 01_errors_vs_exceptions.py

### 📘 What you learn:

- Difference between error and exception
- Runtime error examples

### 🧠 Example:

```python id="py15b1"
# Syntax error example (uncomment to test)
# print("Hello"

a = 10
b = 0

# Runtime error (ZeroDivisionError)
# print(a / b)

print("Program continues safely if handled properly.")
```

---

# 📁 02. try-except Block

## 📄 02_try_except.py

### 📘 What you learn:

- Handling errors using try-except

### 🧠 Example:

```python id="py15b2"
try:
    a = 10
    b = 0
    result = a / b
    print(result)

except:
    print("Error occurred: Cannot divide by zero")

print("Program continues...")
```

---

# 📁 03. Multiple Except Blocks

## 📄 03_multiple_except.py

### 📘 What you learn:

- Handling different errors separately

### 🧠 Example:

```python id="py15b3"
try:
    num = int("abc")
    result = 10 / 0

except ValueError:
    print("Invalid value conversion!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Program finished")
```

---

# 📁 04. else & finally

## 📄 04_else_finally.py

### 📘 What you learn:

- else → runs if no error
- finally → always runs

### 🧠 Example:

```python id="py15b4"
try:
    num = 10
    result = num / 2

except ZeroDivisionError:
    print("Error occurred")

else:
    print("No error occurred:", result)

finally:
    print("This always runs (cleanup code)")
```

---

# 📁 05. raise Exception

## 📄 05_raise_exception.py

### 📘 What you learn:

- Creating custom errors manually

### 🧠 Example:

```python id="py15b5"
age = -5

if age < 0:
    raise ValueError("Age cannot be negative!")

print("Age is valid")
```

---

# 📁 06. Real World Example

## 📄 06_real_world_example.py

### 📘 What you learn:

- Handling user input safely

### 🧠 Example:

```python id="py15b6"
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Please enter a valid number!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print("Result is:", result)

finally:
    print("Execution completed.")
```

---

# 📁 07. Summary File

## 📄 07_exception_summary.py

### 🧠 Example:

```python id="py15b7"
print("Exception Handling Completed 🚀")
```

---

# 🎯 Day 15 Summary

You Learned:

## 🚨 Errors vs Exceptions

✔ Syntax error vs runtime error

## 🛡 try-except

✔ Prevent program crash

## 🔀 Multiple exceptions

✔ Handle different errors separately

## ⚙ else & finally

✔ Success + cleanup blocks

## 🚀 raise

✔ Manually create errors

---

# 🚀 What’s Next?

👉 **Day 16 — Comprehensions in Python**

You will learn:

- List Comprehension
- Dictionary Comprehension
- Set Comprehension
- Nested Comprehension

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
