# 🐍 Python Programming – Day 10: Functions

---

## 📌 Overview

In this chapter, you will learn about **Functions in Python**.

A **function** is a reusable block of code that helps you avoid writing the same code again and again.

---

## 💡 Why Functions Are Important?

- ✔ Code reuse
- ✔ Better organization
- ✔ Easy debugging
- ✔ Cleaner code structure

---

# 🔧 PART 1 — FUNCTION BASICS

---

## 📌 What is a Function?

A function is defined using the `def` keyword.

---

## 📁 01_function_definition.py

```python id="py10b1"
"""
Function Definition:

✔ Function = reusable block of code
✔ Defined using def keyword
"""

def greet():
    print("Hello, welcome to Python Functions!")

greet()
```

---

# 📥 PART 2 — PARAMETERS & ARGUMENTS

---

## 📌 What are Parameters?

- Parameters = variables inside function definition
- Arguments = actual values passed to function

---

## 📁 02_parameters_arguments.py

```python id="py10b2"
"""
Parameters & Arguments:

✔ Pass values into functions
"""

def add(a, b):
    print("Sum:", a + b)

add(10, 20)
add(5, 15)
```

---

# 📤 PART 3 — RETURN VALUES

---

## 📌 What is return?

The `return` keyword sends a result back from a function.

---

## 📁 03_return_values.py

```python id="py10b3"
"""
Return Values:

✔ Function returns result
"""

def multiply(a, b):
    return a * b

result = multiply(4, 5)

print("Result:", result)
```

---

# ⚙ PART 4 — DEFAULT ARGUMENTS

---

## 📌 What are Default Arguments?

If no value is provided, a default value is used.

---

## 📁 04_default_arguments.py

```python id="py10b4"
"""
Default Arguments:

✔ Uses default value if no input given
"""

def greet(name="User"):
    print("Hello", name)

greet("Monjur")
greet()
```

---

# 🔑 PART 5 — KEYWORD ARGUMENTS

---

## 📌 What are Keyword Arguments?

Arguments passed using parameter names.

---

## 📁 05_keyword_arguments.py

```python id="py10b5"
"""
Keyword Arguments:

✔ Order doesn't matter
"""

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=22, name="Monjur")
```

---

# 🌍 PART 6 — VARIABLE SCOPE

---

## 📌 What is Scope?

- Local variable → inside function
- Global variable → outside function

---

## 📁 06_variable_scope.py

```python id="py10b6"
"""
Variable Scope:

✔ Local vs Global variables
"""

x = 100  # global variable

def demo():
    y = 50  # local variable
    print("Inside function (y):", y)
    print("Global variable (x):", x)

demo()

print("Outside function (x):", x)
```

---

# 🎯 DAY 10 SUMMARY

After completing this lesson, you learned:

## 🔧 Functions

- Function definition using `def`
- Code reuse concept

## 📥 Parameters & Arguments

- Passing values into functions

## 📤 Return Values

- Getting output from functions

## ⚙ Default Arguments

- Predefined values

## 🔑 Keyword Arguments

- Named parameters

## 🌍 Variable Scope

- Local vs Global variables

---

# 🚀 Congratulations!

🎉 You have completed:

## 🐍 Python Beginner Series (Day 01 → Day 10)

You now understand:

- Variables
- Loops
- Conditions
- Lists
- Strings
- Functions
- Basic problem solving

---

# 🚀 What’s Next?

👉 **Day 11 — Lambda & Functional Programming in Python**

You will learn:

- Lambda Functions
- `map()`
- `filter()`
- `functools.reduce()`

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


