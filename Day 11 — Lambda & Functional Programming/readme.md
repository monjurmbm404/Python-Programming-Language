# 🐍 Python Programming – Day 11: Lambda & Functional Programming

---

## 📌 Overview

In **Day 11**, you will learn one of the most powerful Python concepts:

### ⚡ Functional Programming Basics

This includes:

* Lambda functions (anonymous functions)
* `map()` function
* `filter()` function
* `reduce()` function
* Functional programming style thinking

---

## 💡 Why this topic is important?

✔ Makes code shorter and cleaner
✔ Widely used in real-world Python projects
✔ Important for data science and backend development
✔ Helps you write “smart” one-line logic

---

# ⚡ 01. Lambda Basics

## 📁 01_lambda_basics.py

### 📘 What you learn:

* What is lambda function
* Difference between normal function and lambda

### 🧠 Example:

```python id="py11b1"
# Normal function
def add(a, b):
    return a + b

print("Normal function:", add(5, 3))

# Lambda function (anonymous function)
add_lambda = lambda a, b: a + b

print("Lambda function:", add_lambda(5, 3))
```

---

# ⚡ 02. Lambda Single Use

## 📁 02_lambda_single_use.py

### 📘 What you learn:

* Using lambda for simple operations

### 🧠 Example:

```python id="py11b2"
square = lambda x: x * x
cube = lambda x: x ** 3

print("Square:", square(4))
print("Cube:", cube(3))
```

---

# 🗺 03. map() Function

## 📁 03_map_function.py

### 📘 What you learn:

* Apply function to every element in a list

### 🧠 Example:

```python id="py11b3"
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("Original:", numbers)
print("Squares:", squares)
```

---

# 🎯 04. filter() Function

## 📁 04_filter_function.py

### 📘 What you learn:

* Filter elements based on condition

### 🧠 Example:

```python id="py11b4"
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", evens)
```

---

# 🔥 05. reduce() Function

## 📁 05_reduce_function.py

### 📘 What you learn:

* Reduce list into a single value
* Uses `functools` module

### 🧠 Example:

```python id="py11b5"
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)
product = reduce(lambda x, y: x * y, numbers)

print("Sum:", result)
print("Product:", product)
```

---

# 🧠 06. Functional Programming Concept

## 📁 06_functional_programming_concept.py

### 📘 What you learn:

* Combining map + filter + lambda
* Functional programming style

### 🧠 Example:

```python id="py11b6"
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))
even_squares = list(filter(lambda x: x % 2 == 0, squares))

print("Original:", numbers)
print("Squares:", squares)
print("Even Squares:", even_squares)
```

---

# 🎯 Day 11 Summary

You Learned:

## ⚡ Lambda Functions

✔ Anonymous one-line functions   
✔ Quick operations

## 🗺 map()

✔ Apply function to all elements

## 🎯 filter()

✔ Filter data based on condition

## 🔥 reduce()

✔ Convert list into single value

## 🧠 Functional Programming

✔ Combine map + filter + lambda

---

# 🚀 What’s Next?

👉 **Day 12 — Iterators & Generators  in Python**

You will learn:

- Iterator Concept
- `iter()` and `next()`
- Generator (`yield`)
- Generator vs Normal Function

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


