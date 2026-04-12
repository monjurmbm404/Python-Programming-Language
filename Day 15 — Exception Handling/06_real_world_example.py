"""
========================================
06_real_world_example.py
========================================
Real-world Exception Handling:

✔ User input handling
"""

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