"""
========================================
05_continue_statement.py
========================================
continue Statement:

✔ Skips current iteration
✔ Moves to next iteration
"""

for i in range(1, 6):
    if i == 3:
        print("Skipped:", i)
        continue
    print("Value:", i)