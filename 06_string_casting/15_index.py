# ********** index **********

"""
index(substring, start, end)

The index() method returns the index of the first occurrence of a substring in a string — just like 
find(), but...
       ⚠️ If the substring is not found, it raises a ValueError instead of returning -1.

✅ Syntax:
string.index(substring)

Optional:
string.index(substring, start, end)

- substring: What you want to locate
- start, end: (optional) Slice range to search within


Comparison with find():

| Feature            | find()             | index()               |
|--------------------|--------------------|------------------------|
| Returns index      | ✅ Yes             | ✅ Yes                 |
| Case-sensitive     | ✅ Yes             | ✅ Yes                 |
| If not found       | Returns -1         | ❌ Raises ValueError   |
| Safe for searching | ✅ Safer to use    | ⚠️ Use try-except      |

"""

# ✅ Example 1: Basic usage
text = "Hello, World!"

# ✅ It found "World" starting at index 7.
print(text.index("World"))  # Output: 7

# ✅ Example 2: When the substring is not found
text = "Hello, World!"

# 🚫 It raises a ValueError because "Python" is not in the string.
# ⚠️ Unlike find(), this raises an error instead of returning -1.
# print(text.index("Python"))  # Output: ValueError: substring not found

# ✅ Example 3: Case sensitivity
text = "Hello, world!"
# Case must match exactly — just like find().
print(text.index("world"))  # Output: 7

# ✅ Example 4: With start and end indexes
text = "banana"
print(text.index("a", 2))  # Start searching from index 2 and Output: 3
