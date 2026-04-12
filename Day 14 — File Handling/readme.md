# 📂 Python Programming – Day 14: File Handling

---

## 📌 Overview

In **Day 14**, you will learn how to work with **files in Python**.

File handling allows your program to:

- 📁 Store data permanently
- 📖 Read saved information
- ✍️ Write and update files
- 🔄 Append new data
- 📍 Control file reading position

---

## 💡 Why File Handling is Important?

✔ Used in real-world applications  
✔ Saves user data permanently  
✔ Used in logs, databases, reports  
✔ Important for backend development

---

# 📁 01. File Opening

## 📄 01_file_opening.py

### 📘 What you learn:

- How to open a file
- Reading file content
- Closing a file properly

### 🧠 Example:

```python id="py14b1"
file = open("sample.txt", "r")

content = file.read()

print("File Content:")
print(content)

file.close()
```

---

# 📁 02. File Modes

## 📄 02_file_modes.py

### 📘 What you learn:

- Different file modes

### 🔑 Modes:

- `r` → read
- `w` → write (overwrite)
- `a` → append

### 🧠 Example:

```python id="py14b2"
file = open("demo.txt", "w")
file.write("This is write mode.\n")
file.close()

file = open("demo.txt", "a")
file.write("This is append mode.\n")
file.close()

file = open("demo.txt", "r")
print(file.read())
file.close()
```

---

# 📁 03. Reading Files

## 📄 03_read_file.py

### 📘 What you learn:

- Different ways to read files

### 🧠 Methods:

- `read()` → full file
- `readline()` → one line
- `readlines()` → list of lines

### 🧠 Example:

```python id="py14b3"
file = open("demo.txt", "r")

print(file.read())

file.close()

file = open("demo.txt", "r")

print(file.readline())
print(file.readline())

file.close()
```

---

# 📁 04. Write & Append

## 📄 04_write_append.py

### 📘 What you learn:

- Writing new data
- Appending data safely

### 🧠 Example:

```python id="py14b4"
with open("data.txt", "w") as file:
    file.write("Hello Python\n")

with open("data.txt", "a") as file:
    file.write("Adding more data\n")

with open("data.txt", "r") as file:
    print(file.read())
```

---

# 📁 05. File Pointer

## 📄 05_file_pointer.py

### 📘 What you learn:

- Track file position
- Move reading cursor

### 🔑 Methods:

- `tell()` → current position
- `seek()` → move position

### 🧠 Example:

```python id="py14b5"
with open("data.txt", "r") as file:

    print(file.tell())

    print(file.read(5))
    print(file.tell())

    file.seek(0)

    print(file.read())
```

---

# 📁 06. With Statement (Best Practice)

## 📄 06_with_statement.py

### 📘 What you learn:

- Auto file closing
- Cleaner code

### 🧠 Example:

```python id="py14b6"
with open("example.txt", "w") as file:
    file.write("Using with statement\n")

with open("example.txt", "r") as file:
    print(file.read())
```

---

# 📁 07. Real Practice Example

## 📄 07_text_file_practice.py

### 📘 What you learn:

- Working with real text files
- Counting lines
- Cleaning output

### 🧠 Example:

```python id="py14b7"
with open("notes.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("Day 14 Learning\n")
    file.write("Practice is important\n")

with open("notes.txt", "r") as file:
    lines = file.readlines()

print("Total Lines:", len(lines))

for line in lines:
    print(line.strip())
```

---

# 📁 08. Summary

## 📄 08_file_handling_summary.py

### 🧠 Example:

```python id="py14b8"
print("File Handling Completed 🚀")
```

---

# 🎯 Day 14 Summary

You Learned:

## 📂 File Basics

✔ open() function  
✔ File modes (r, w, a)

## 📖 Reading Files

✔ read()  
✔ readline()  
✔ readlines()

## ✍ Writing Files

✔ write mode  
✔ append mode

## 📍 File Pointer

✔ tell()  
✔ seek()

## ⚡ Best Practice

✔ Use `with` statement

---

# 🚀 What’s Next?

👉 **Day 15 — Exception Handling in Python**

You will learn:

- Errors vs Exceptions
- `try`, `except`
- Multiple except
- `else`, `finally`
- `raise`

---

# Author

**Engr. Md Monjur Bakth Mazumder**

🎓 Diploma in Computer Science and Technology — [Moulvibazar Polytechnic Institute](https://mpi.moulvibazar.gov.bd/)  
🎓 BSc in Computer Science & Engineering (CSE) (Ongoing) — [Sylhet International University](https://siu.edu.bd/)

📧 Email: monjurmbm404@gmail.com

### ⭐ If you find this helpful, don’t forget to **star** the repository!
