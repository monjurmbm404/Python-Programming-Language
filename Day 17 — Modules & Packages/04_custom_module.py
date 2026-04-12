"""
========================================
04_custom_module.py
========================================
Create Custom Module:

✔ You can create your own .py file
✔ Then import it into another file
"""

# Suppose we created a file: mymodule.py
# with function:

# def greet(name):
#     return "Hello " + name

# Now importing it
import mymodule

print(mymodule.greet("Monjur"))