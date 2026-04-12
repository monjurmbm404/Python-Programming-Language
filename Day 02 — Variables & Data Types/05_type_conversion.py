"""
========================================
05_type_conversion.py
========================================
Type Conversion:

✔ Convert one type to another
✔ Common functions:
   int(), float(), str(), bool()
"""

# String to int
a = "10"
b = int(a)
print(b, type(b))

# int to float
x = 5
y = float(x)
print(y, type(y))

# float to int
p = 3.99
q = int(p)  # decimal part removed
print(q, type(q))

# int to string
num = 100
text = str(num)
print(text, type(text))

# boolean conversion
print(bool(0))     # False
print(bool(1))     # True
print(bool(""))    # False
print(bool("Hi"))  # True