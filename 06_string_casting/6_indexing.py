"""
String Indexing in Python
--------------------------

In Python, strings are sequences of characters, and each character has an index (position) that you can use to access it.

Indexing allows you to **retrieve individual characters** from a string using square brackets `[]`.

Types of Indexing:
-------------------
1. **Forward Indexing** (starts from 0):
   Each character is assigned a position from left to right.

   Example:
       text = "Python"
       text[0] => 'P'
       text[1] => 'y'

2. **Backward Indexing** (starts from -1):
   Indexing also works from right to left using negative numbers.

   Example:
       text = "Python"
       text[-1] => 'n'
       text[-2] => 'o'

Examples:
----------
text = "Python"

text[0]       # 'P'  (first character)
text[3]       # 'h'  (fourth character)
text[-1]      # 'n'  (last character)
text[-4]      # 't'  (third character from the end)

Notes:
-------
- Indexes must be within the valid range. Accessing an index outside the range will raise an `IndexError`.

    text[100]  # ❌ IndexError

- Strings are **immutable** — you cannot change individual characters by assignment.

    text[0] = "J"  # ❌ TypeError

To change a string, create a new one using slicing or concatenation.

    new_text = "J" + text[1:]  # ✅ Jython

"""

# 1. Accessing characters with positive indices
text = "Python"
print(text[0])  # Output: P
print(text[3])  # Output: h

# 2. Accessing characters with negative indices
print(text[-1])  # Output: n
print(text[-4])  # Output: t

# 3. Invalid index (out of range)
# print(text[10])  # ❌ IndexError: string index out of range


# You cannot change characters in a string like this:
# text[0] = "J"  # ❌ TypeError

# Instead, you must create a new string:
new_text = "J" + text[1:]  # ✅ Jython
print(new_text)  # Output: Jython
