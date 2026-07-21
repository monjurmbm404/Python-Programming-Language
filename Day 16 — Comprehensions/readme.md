# 🐍 Python Programming – Day 16: Comprehensions

---

## 📌 Overview

In **Day 16**, you will learn one of the most powerful and Pythonic concepts:

# ⚡ Comprehensions

Comprehensions allow you to create:

- 📋 Lists
- 📦 Dictionaries
- 🧩 Sets

in a **short, clean, and readable way**.

---

## 💡 Why Comprehensions are Important?

✔ Reduce code length  
✔ Improve readability  
✔ Faster than normal loops  
✔ Widely used in real-world Python projects  
✔ Important for interviews and coding tests

---

# 📁 01. List Comprehension

## 📄 01_list_comprehension.py

### 📘 What you learn:

- Create lists in one line
- Apply conditions inside lists

### 🧠 Example:

```python id="py16b1"
numbers = [i for i in range(1, 6)]
print(numbers)

squares = [i * i for i in range(1, 6)]
print(squares)

evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)
```

---

# 📁 02. Dictionary Comprehension

## 📄 02_dictionary_comprehension.py

### 📘 What you learn:

- Create dictionaries in one line
- Key-value generation

### 🧠 Example:

```python id="py16b2"
square_dict = {i: i * i for i in range(1, 6)}
print(square_dict)

even_dict = {i: i for i in range(1, 11) if i % 2 == 0}
print(even_dict)
```

---

# 📁 03. Set Comprehension

## 📄 03_set_comprehension.py

### 📘 What you learn:

- Create sets using comprehension
- Automatic removal of duplicates

### 🧠 Example:

```python id="py16b3"
nums = {i * 2 for i in range(1, 6)}
print(nums)

unique_squares = {i * i for i in range(1, 6)}
print(unique_squares)
```

---

# 📁 04. Nested Comprehension

## 📄 04_nested_comprehension.py

### 📘 What you learn:

- Comprehension inside comprehension
- Matrix creation

### 🧠 Example:

```python id="py16b4"
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)
```

---

# 📁 05. Comprehension with Conditions

## 📄 05_comprehension_with_condition.py

### 📘 What you learn:

- Filtering inside comprehension
- Combining condition + expression

### 🧠 Example:

```python id="py16b5"
result = [i * i for i in range(1, 11) if i % 2 == 0]
print(result)

words = ["apple", "banana", "cherry", "kiwi"]
filtered = [word.upper() for word in words if len(word) > 5]

print(filtered)
```

---

# 📁 06. Summary

## 📄 06_comprehension_summary.py

### 🧠 Example:

```python id="py16b6"
print("Comprehensions Completed 🚀")
```

---

# 🎯 Day 16 Summary

You Learned:

## 📋 List Comprehension

✔ One-line list creation  
✔ With conditions

## 📦 Dictionary Comprehension

✔ Key-value generation

## 🧩 Set Comprehension

✔ Unique values automatically

## 🔁 Nested Comprehension

✔ Matrix-style structures

---

# ⚡ Key Benefits

✔ Cleaner code  
✔ Faster execution  
✔ Pythonic style (very important for interviews)

---

# 🚀 What’s Next?

👉 **Day 17 — Modules & Packages in Python**

You will learn:

- `import`
- `from ... import`
- Built-in Modules (`math`, `random`)
- Create Custom Module
- Package Basics

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

