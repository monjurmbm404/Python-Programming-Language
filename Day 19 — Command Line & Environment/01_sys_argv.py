"""
========================================
01_sys_argv.py
========================================
sys.argv:

✔ Used to pass command-line arguments
✔ sys.argv is a list
✔ argv[0] = script name
"""

import sys

print("Script Name:", sys.argv[0])

# Check if arguments are passed
if len(sys.argv) > 1:
    print("Arguments:")
    
    for i in range(1, len(sys.argv)):
        print(f"Arg {i}:", sys.argv[i])
else:
    print("No arguments provided")