"""
========================================
06_palindrome_check.py
========================================
Palindrome Check:

✔ A string is palindrome if it reads same forward & backward
"""

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")