# 🐍 Python Programming – Day 07: Lists

---

## 📌 Overview

In this chapter, you will learn about **Lists in Python**.

A list is one of the most important data structures in Python.

### 💡 Key Features of Lists:

- Stores multiple values in one variable 📦
- Can store different data types
- Ordered (has index) 📍
- Mutable (can be changed) ✏️

---

# 📦 01. List Basics

## 📁 01_list_basics.py

### 📘 What you learn:

- Creating lists
- Storing multiple values
- Mixed data types

### 🧠 Example:

```python id="py7b1"
numbers = [10, 20, 30, 40, 50]
print(numbers)

mixed = [10, "Python", 3.14, True]
print(mixed)
```

---

# 📍 02. Indexing & Slicing

## 📁 02_indexing_slicing.py

### 📘 What you learn:

- Access elements using index
- Slice parts of list

### 🧠 Example:

```python id="py7b2"
arr = [10, 20, 30, 40, 50]

print(arr[0])     # first element
print(arr[-1])    # last element

print(arr[0:3])   # slicing
print(arr[::-1])  # reverse list
```

---

# 🛠️ 03. List Methods

## 📁 03_list_methods.py

### 📘 What you learn:

Important built-in functions for lists

### 🧠 Example:

```python id="py7b3"
nums = [3, 1, 4, 2]

nums.append(5)
nums.insert(1, 10)
nums.remove(10)
nums.pop()

nums.sort()
nums.reverse()
```

---

# 🔁 04. Looping Through Lists

## 📁 04_looping_lists.py

### 📘 What you learn:

- Loop through list using for loop

### 🧠 Example:

```python id="py7b4"
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

---

# 📊 05. List Operations

## 📁 05_list_operations.py

### 📘 What you learn:

- Basic math operations on list

### 🧠 Example:

```python id="py7b5"
numbers = [10, 20, 30, 40]

print(sum(numbers))
print(max(numbers))
print(min(numbers))
```

---

# 🔍 06. List Searching

## 📁 06_list_searching.py

### 📘 What you learn:

- Finding elements using loop (Linear Search)

### 🧠 Example:

```python id="py7b6"
arr = [10, 20, 30, 40, 50]
target = 30

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index:", i)
        break
```

---

# 📈 07. List Sorting

## 📁 07_list_sorting.py

### 📘 What you learn:

- Sorting lists in ascending & descending order

### 🧠 Example:

```python id="py7b7"
nums = [50, 10, 40, 20, 30]

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)
```

---

# 🎯 Day 07 Summary

After completing this day, you learned:

✅ List Basics  
✅ Indexing & Slicing  
✅ List Methods  
✅ Looping Through Lists  
✅ Sum, Max, Min  
✅ Linear Search  
✅ Sorting

---

## 🚀 What’s Next?

Next step:
👉 **Day 08 — Tuple, Set, Dictionary in Python**

You’ll learn:

- Tuple
  - Immutable concept
  - Packing & Unpacking

- Set
  - Unique elements
  - Set operations

- Dictionary
  - Key-value pairs
  - Access, update, delete
  - Looping

---

> 💡 **Pro Tip:**
> Lists are one of the MOST used concepts in real-world Python projects. Practice them daily!

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

