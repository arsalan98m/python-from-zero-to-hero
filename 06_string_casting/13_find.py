"""
find(substring)

The find() method returns the index (position) of the first occurrence of a specified substring.

If the substring is not found, it returns -1.

string.find(substring, start, end)

- substring: What you're searching for
- start (optional): Index to start searching from
- end (optional): Index to stop searching
"""

# ✅ Example 1: Find a word
# 🧠 "World" starts at index 7.
text = "Hello, World!"
index = text.find("World")
print(index)  # Output: 7


# ✅ Example 2: Substring not found
# 🚫 Returns -1 because "Python" is not in the string.
text = "Hello, World!"
index = text.find("Python")
print(index)  # Output: -1


# ✅ Example 3: Case-sensitive search
# ⚠️ It didn’t find "world" because "World" has a capital "W" — find() is case-sensitive.
text = "Hello, World!"
print(text.find("world"))  # Output: -1

# ✅ Example 4: Find with start and end positions
# 🔎 It finds the first "a" after index 2.
text = "banana"
print(text.find("a", 2))  # Start searching from index 2 and it Output: 3
