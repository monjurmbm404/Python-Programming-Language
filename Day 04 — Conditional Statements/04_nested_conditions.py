"""
========================================
04_nested_conditions.py
========================================
Nested Conditions:

✔ if inside another if
✔ used for complex decision making
"""

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed to enter")
    else:
        print("ID required")
else:
    print("Not allowed (underage)")