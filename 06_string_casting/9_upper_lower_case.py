"""
String Case Conversion in Python
--------------------------------

Python provides built-in string methods to change the case of letters:

1. `upper()` → Converts all characters in a string to **uppercase**.
2. `lower()` → Converts all characters in a string to **lowercase**.

These methods:
- Return a **new string** (they do not modify the original).
- Work only on alphabetic characters. Numbers and symbols are left unchanged.

Syntax:
--------
    string.upper()
    string.lower()

Examples:
----------
text = "Hello World"

text.upper()     => 'HELLO WORLD'
text.lower()     => 'hello world'

Notes:
-------
- These methods are useful for formatting user input, case-insensitive comparisons, and standardizing output.
- Strings are immutable, so use reassignment if you want to store the result.

    name = "Arsalan"
    name = name.upper()  # Reassign if needed

"""

text = "Hello World"
print(text.upper())  # Output: HELLO WORLD
print(text.lower())  # Output: hello world
