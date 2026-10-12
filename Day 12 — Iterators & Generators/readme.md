# 🐍 Python Programming – Day 12: Iterators & Generators

---

## 📌 Overview

In **Day 12**, you will learn two very important advanced Python concepts:

### 🔁 Iterators

### ⚡ Generators

These concepts help you work with data efficiently, especially when dealing with loops and large datasets.

---

## 💡 Why this topic is important?

✔ Helps you understand how Python loops work internally   
✔ Improves memory efficiency   
✔ Very useful in real-world applications (data processing, APIs, ML, etc.)   
✔ Important for interviews   

---

# 🔁 PART 1 — ITERATORS

---

## 📁 01_iterator_concept.py

### 📘 What you learn:

- What is an iterator
- How to use `iter()` and `next()`

### 🧠 Example:

```python id="py12b1"
numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
```

---

## 📁 02_iter_next_function.py

### 📘 What you learn:

- Iterating strings using iterator
- Working character by character

### 🧠 Example:

```python id="py12b2"
text = "Python"

it = iter(text)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
```

---

## 📁 03_custom_iterator.py

### 📘 What you learn:

- Creating your own iterator using a class

### 🧠 Example:

```python id="py12b3"
class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

obj = MyNumbers()

for i in obj:
    print(i)
```

---

# ⚡ PART 2 — GENERATORS

---

## 📁 04_generator_basic.py

### 📘 What you learn:

- What is generator
- `yield` keyword

### 🧠 Example:

```python id="py12b4"
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))
```

---

## 📁 05_generator_with_loop.py

### 📘 What you learn:

- Generator with loop
- Producing values step by step

### 🧠 Example:

```python id="py12b5"
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for value in count_up_to(5):
    print(value)
```

---

## 📁 06_generator_vs_function.py

### 📘 What you learn:

- Difference between return and yield

### 🧠 Example:

```python id="py12b6"
def normal_function():
    return [1, 2, 3]

def generator_function():
    yield 1
    yield 2
    yield 3

print("Normal function:", normal_function())

for value in generator_function():
    print(value)
```

---

## 📁 07_memory_efficiency_demo.py

### 📘 What you learn:

- Why generators are memory efficient

### 🧠 Example:

```python id="py12b7"
def large_range(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = large_range(1000000)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
```

---

# 🎯 Day 12 Summary

## 🔁 Iterators

✔ iter() → creates iterator  
✔ next() → gets next value  
✔ Custom iterator class

---

## ⚡ Generators

✔ Uses `yield` instead of return  
✔ Produces values one by one  
✔ Memory efficient

---

## 🔥 Key Difference

| Function | Behavior                    |
| -------- | --------------------------- |
| return   | returns everything at once  |
| yield    | returns values step by step |

---

# 🚀 What’s Next?

👉 **Day 13 — Recursion in Python**

You will learn:

- Recursion Concept
- Base Case
- Factorial
- Fibonacci
- Problem Solving

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


