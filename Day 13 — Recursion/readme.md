# 🐍 Python Programming – Day 13: Recursion

---

## 📌 Overview

In **Day 13**, you will learn one of the most important programming concepts:

# 🔁 Recursion

Recursion is a technique where a **function calls itself** to solve a problem.

---

## 💡 Why this topic is important?

✔ Helps solve complex problems easily  
✔ Used in algorithms (sorting, searching, trees, graphs)  
✔ Important for coding interviews  
✔ Builds strong logical thinking

---

# ⚠️ Important Rule of Recursion

Every recursive function must have:

### 🚪 Base Case

✔ Stops the recursion  
✔ Prevents infinite loop

### 🔁 Recursive Case

✔ Function calls itself

---

# 🔁 01. Recursion Concept

## 📁 01_recursion_concept.py

### 📘 What you learn:

- Basic idea of recursion
- Function calling itself

### 🧠 Example:

```python id="py13b1"
def greet(n):
    if n == 0:
        return
    print("Hello Recursion")
    greet(n - 1)

greet(5)
```

---

# 🚪 02. Base Case

## 📁 02_base_case.py

### 📘 What you learn:

- How recursion stops safely

### 🧠 Example:

```python id="py13b2"
def countdown(n):
    if n == 0:
        print("Done!")
        return

    print("Count:", n)
    countdown(n - 1)

countdown(5)
```

---

# 🧮 03. Factorial Using Recursion

## 📁 03_factorial_recursion.py

### 📘 What you learn:

- Mathematical recursion problem

### 🧠 Formula:

```
n! = n × (n - 1)!
0! = 1
```

### Example:

```python id="py13b3"
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))
```

---

# 🔢 04. Fibonacci Series

## 📁 04_fibonacci_recursion.py

### 📘 What you learn:

- Famous recursion problem

### 🧠 Formula:

```
F(n) = F(n-1) + F(n-2)
```

### Example:

```python id="py13b4"
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")
```

---

# 🧠 05. Recursive Problem Solving

## 📁 05_recursive_problem_solving.py

### 📘 What you learn:

- Breaking problems into smaller parts

### 🧠 Example:

```python id="py13b5"
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

print("Sum:", sum_numbers(5))


def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

print("Reversed:", reverse_string("Python"))
```

---

# ⚡ 06. Recursion vs Loop

## 📁 06_recursion_vs_loop.py

### 📘 What you learn:

- Difference between recursion and loops

### 🧠 Example:

```python id="py13b6"
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)

print("Loop:", factorial_loop(5))
print("Recursion:", factorial_rec(5))
```

---

# 🎯 Day 13 Summary

## 🔁 Recursion

✔ Function calls itself  
✔ Must have base case

---

## 🚪 Base Case

✔ Stops recursion safely

---

## 🧮 Problems You Learned

✔ Factorial  
✔ Fibonacci  
✔ Sum of numbers  
✔ String reversal

---

## ⚖️ Recursion vs Loop

| Feature | Recursion | Loop   |
| ------- | --------- | ------ |
| Speed   | Slower    | Faster |
| Code    | Clean     | Simple |
| Memory  | Higher    | Lower  |

---

# 🚀 What’s Next?

👉 **Day 14 — File Handling in Python**

You will learn:

- File Opening
- Modes: `r`, `w`, `a`
- Read / Write / Append
- File Pointer (`tell`, `seek`)
- Working with Text Files

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

