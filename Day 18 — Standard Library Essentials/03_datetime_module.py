"""
========================================
03_datetime_module.py
========================================
datetime Module:

✔ Handles date and time
"""

import datetime

# Current date & time
now = datetime.datetime.now()
print("Current DateTime:", now)

# Current date
today = datetime.date.today()
print("Today:", today)

# Custom date
custom_date = datetime.date(2026, 4, 12)
print("Custom Date:", custom_date)

# Formatting date
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))