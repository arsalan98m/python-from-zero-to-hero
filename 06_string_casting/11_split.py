"""
split(delimiter)

If you use split() without passing a delimiter, Python will use any whitespace 
(spaces, tabs, newlines) as the default separator and automatically ignore extra 
whitespace between words.

It means:

`Split this string wherever there is any kind of space — like a normal space 
(' '), tab (\t), or newline (\n). And if there are multiple spaces in a row,
just treat them as one.



✅ Key Points:
- `split()` without an argument is the same as `split(None)` — it splits on any whitespace.
- It automatically handles multiple spaces or tabs:
"""

# ✅ Example 1: Normal usage
text = "Hello World!"
print(text.split())  # Output: ['Hello', 'World']


# ✅ Example 2: Multiple spaces between words
# ✅ Even though there are 10 spaces, Python ignores the extra ones and treats them like just 1.
text = "Hello          World from Python"
print(text.split())  # Output: ['Hello', 'World', 'from', 'Python']

# ✅ Example 3: Tabs and newlines
# ✅ It splits the string at both tab (\t) and newline (\n), or space.
text = "Hello\tWo rld\nPython"
print(text.split())  # Output: ['Hello', 'Wo', 'rld', 'Python']

"""
If you do pass a specific delimiter, it only splits on that exact character, and 
won't skip extra delimiters.

It means:
- Python will split the string only where that exact character appears.
- If the delimiter repeats (like ,, or ll), Python will not ignore the empty part 
between them — it will include it as an empty string '' in the result.

🔁 Summary:
- split(',') → splits only at commas.
- It does not ignore extra or repeated commas.
- If there's nothing between two commas, it adds an empty string in the result.

"""

# ✅ Example 1: Using a specific delimiter(,)
text = "apple,banana,orange"
print(text.split(","))  # Output: ['apple', 'banana', 'orange']

# ✅ Example 2: Repeated delimiter(l)
text = "Hello, World!"
print(text.split("l"))  # Output: ['He', '', 'o', ' Wor', 'd!']

# ✅ Example 3: Repeated delimiter(,)
text = "apple,,orange"
print(text.split(","))  # Output: ['apple', '', 'orange']

# ✅ Example 4: Repeated delimiter(" ")
text = "apple    orange"
print(text.split(" "))  # Output: ['apple', '', '', '', 'orange']
