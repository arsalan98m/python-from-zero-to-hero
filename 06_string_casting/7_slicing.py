"""
String Slicing in Python
-------------------------

Slicing allows you to extract a **portion (substring)** of a string using the syntax:

    string[start:stop:step]

- `start` → The index to begin the slice (inclusive).
- `stop`  → The index to end the slice (exclusive).
- `step`  → Optional. Defines the increment (default is 1).

If any part is omitted:
- `start` defaults to the beginning (0).
- `stop` defaults to the end of the string.
- `step` defaults to 1.

Examples:
----------
text = "Python"

text[0:2]       => 'Py'     # From index 0 to 1
text[1:5]       => 'ytho'   # From index 1 to 4
text[:3]        => 'Pyt'    # From start to index 2
text[3:]        => 'hon'    # From index 3 to end
text[:]         => 'Python' # Entire string
text[::2]       => 'Pto'    # Every 2nd character
text[::-1]      => 'nohtyP' # Reversed string

Notes:
-------
- Slicing **never throws an error** for out-of-range indices; it adjusts silently.
- Negative indices can also be used in slicing.
- Strings remain immutable — slicing returns a **new string**.

"""

# ✅ 1. Basic Slicing: string[start:stop]
text = "Python"
print(text[0:2])  # Output: 'Py' (characters at index 0 and 1)
print(text[1:5])  # Output: 'ytho' (index 1 to 4)

# ✅ 2. Omitting Start or Stop
print(text[:3])  # Output: 'Pyt' (from start to index 2)
print(text[3:])  # Output: 'hon' (from index 3 to end)
print(text[:])   # Output: 'Python' (full string)

# ✅ 3. Using Step
print(text[::2])   # Output: 'Pto' (every second character)
print(text[1::2])  # Output: 'yhn' (start at index 1, step by 2)

# ✅ 4. Negative Indices
print(text[-4:-1])   # Output: 'tho' (index -4 to -2)
print(text[-6:-3])   # Output: 'Pyt' (same as text[0:3])

# ✅ 5. Reversing a String
print(text[::-1])   # Output: 'nohtyP'

# ✅ 6. Slicing Beyond Bounds (No error)
print(text[0:100])    # Output: 'Python' (adjusts automatically)
print(text[-100:2])   # Output: 'Py'
print(text[-100:-2])  # Output: 'Pyth'
