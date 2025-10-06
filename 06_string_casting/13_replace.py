"""
replace(old, new)

The `replace()` method is used to replace a specific substring in a string with another substring.

- `old`: The substring you want to replace.
- `new`: The substring you want to insert in its place.

"""

# ✅ Example 1: Basic replacement
text = "I love apples"
new_text = text.replace("apples", "mangoes")
print(new_text)  # Output: I love mangoes

# ✅ Example 2: Replace all occurrences
text = "Ha Ha Ha ha"
new_text = text.replace("Ha", "Ho")
print(new_text)  # Output: Ho Ho Ho ha

# ✅ Example 3: Replace with empty string (used to remove something)
# 🧹 This is a handy trick to remove unwanted characters like commas, extra spaces, or symbols.
text = "Hello, World!"
clean_text = text.replace(",", "")
print(clean_text)  # Output: Hello World!

# ✅ Example 4: Case sensitivity
# 🔎 Python is case-sensitive — "Hello" and "hello" are treated differently.
text = "Hello hello"
print(text.replace("hello", "hi"))  # Output: Hello hi

# ✅ Optional: Limit how many times it replaces
# 💡 The 2 at the end tells Python to replace only the first 2 occurrences.

text = "one one one"
new_text = text.replace("one", "two", 2)
print(new_text)  # Output: two two one
