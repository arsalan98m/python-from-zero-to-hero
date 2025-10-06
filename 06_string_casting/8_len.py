"""
The len() Function in Python
----------------------------

`len()` is a built-in Python function used to return the **number of items** in an object.

For strings, `len()` returns the **number of characters** in the string.

Syntax:
--------
    len(object)

Parameters:
------------
- object: A sequence (like a string, list, tuple) or a collection (like a dictionary, set).

Returns:
---------
- An integer representing the number of elements in the object.

Examples:
----------
# For Strings
len("Python")         => 6

# For Lists
len([1, 2, 3])        => 3

# For Tuples
len(("a", "b"))       => 2

# For Dictionaries
len({"a": 1, "b": 2}) => 2

Notes:
-------
- You cannot use `len()` on numbers (int or float); it raises a TypeError.
- Useful for loops, validations, and slicing logic.
"""

# ✅ 1. Basic len() usage with strings
text = "Python"
print(len(text))  # Output: 6

# ✅ 2. Length of an empty string
empty = ""
print(len(empty))  # Output: 0

# ✅ 3. Length including spaces and special characters
message = "Hello, World!"
print(len(message))  # Output: 13 (includes comma, space, and exclamation mark)

# ✅ 4. Length of a multiline string
quote = """Learning
Python
is
fun!"""
print(len(quote))  # Output includes line breaks (\n)

# ✅ 5. Using len() to get the last character using indexing
name = "Arsalan"
last_char = name[len(name) - 1]
print("Last character:", last_char)  # Output: n
