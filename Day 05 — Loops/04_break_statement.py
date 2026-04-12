"""
========================================
04_break_statement.py
========================================
break Statement:

✔ Stops the loop immediately
"""

for i in range(1, 10):
    if i == 5:
        print("Loop stopped at", i)
        break
    print(i)