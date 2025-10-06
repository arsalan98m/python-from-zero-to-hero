"""
count():

The count() method returns the number of times a specified substring appears in a string.

If you pass a substring that's not in the string, it returns 0.

✅ Syntax:
string.count(substring)

Optional:
string.count(substring, start, end)

- substring: The string or character you want to count
- start (optional): Index to start counting from
- end (optional): Index to stop counting

⚠️ If the substring is not found, count() returns 0.

"""

# ✅ Example 1: Count characters
text = "banana"
# 🍌 It counts how many times "a" appears in "banana" → 3 times.
result = text.count("a")
print(result)  # Output: 3

# ✅ Example 2: Count whole words
text = "I love Python. Python is awesome."
# ✅ Counts how many times "Python" appears — exactly 2 times.
print(text.count("Python"))  # Output: 2

# ✅ Example 3: Case sensitivity
text = "Python python PyThon"
# ⚠️ count() is case-sensitive, so only exact matches count.
print(text.count("Python"))  # Output: 1

# ✅ Example 4: Count with a range
text = "banana"
# 📍 It only looks at the slice "nan" (index 2 to 4) → 1 "a".
print(text.count("a", 2, 5))  # From index 2 to 4 because 5 is not included

# 🔍 What happens when count() doesn’t find the substring?
# If the substring doesn't exist in the string, count() simply returns **0**.
# count() → safely returns 0 if not found ✅
text = "banana"
print(text.count("A"))  # Output: 0
