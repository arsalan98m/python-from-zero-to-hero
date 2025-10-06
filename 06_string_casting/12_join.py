"""
`join() method`

join() method in Python, It's used to join a list of strings into a single string,
using a separator of your choice.


"separator".join(iterable)

The "separator" is the string that will be placed between each item in the list.

🚫 Remember:
- All elements in the list must be strings. If not, you'll get a TypeError.

nums = [1, 2, 3]
" ".join(nums)  # ❌ Error!
"""

# ✅ Example 1: Join with space
words = ["Hello", "World"]
result = " ".join(words)
print(result)  # Output: Hello World

# ✅ Example 2: Join with hyphen
words = ["2025", "07", "12"]
result = "-".join(words)
print(result)  # Output: 2025-07-12

# ✅ Example 3: Join with empty string (used for removing spaces or joining characters)
"""
Join with an empty string "" is commonly used to:
- Combine characters in a list into one string without any separator
- Remove spaces or unwanted characters after splitting
"""

# The empty string "" is used as the glue — so no space, no dash, nothing between characters.
chars = ['a', 'b', 'c']
result = "".join(chars)
print(result)  # Output: abc

# ✅ Example 4: Remove spaces from a string
# text.split() turns the string into: ['Hello', 'World']
# ''.join(...) combines it back without any spaces
text = "Hello World"
no_spaces = "".join(text.split())
print(no_spaces)  # Output: HelloWorld
