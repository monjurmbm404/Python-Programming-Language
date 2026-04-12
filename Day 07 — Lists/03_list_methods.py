"""
========================================
03_list_methods.py
========================================
List Methods:

✔ append()   -> add element
✔ insert()   -> add at position
✔ remove()   -> remove value
✔ pop()      -> remove index
✔ clear()    -> remove all
✔ sort()     -> sort list
✔ reverse()  -> reverse list
"""

nums = [3, 1, 4, 2]

nums.append(5)
print("After append:", nums)

nums.insert(1, 10)
print("After insert:", nums)

nums.remove(10)
print("After remove:", nums)

nums.pop()
print("After pop:", nums)

nums.sort()
print("Sorted:", nums)

nums.reverse()
print("Reversed:", nums)