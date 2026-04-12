"""
========================================
02_base_case.py
========================================
Base Case:

✔ Stops recursion
✔ Prevents infinite calls
"""

def countdown(n):
    if n == 0:
        print("Done!")
        return

    print("Count:", n)
    countdown(n - 1)

countdown(5)