"""
========================================
07_list_sorting.py
========================================
Sorting:

✔ sort() -> ascending
✔ reverse sort -> descending
"""

nums = [50, 10, 40, 20, 30]

# Ascending order
nums.sort()
print("Ascending:", nums)

# Descending order
nums.sort(reverse=True)
print("Descending:", nums)

# Without modifying original
nums2 = sorted(nums)
print("Sorted copy:", nums2)