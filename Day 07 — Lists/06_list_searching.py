"""
========================================
06_list_searching.py
========================================
Searching in List:

✔ Linear search approach
"""

arr = [10, 20, 30, 40, 50]
target = 30

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")