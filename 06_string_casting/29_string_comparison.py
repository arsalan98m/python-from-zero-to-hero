# ********** String Comparisons **********

"""
Comparison Operators for Strings in Python
------------------------------------------

In Python, strings can be compared using standard comparison operators.
These comparisons are based on **lexicographical order**, which means
they follow the Unicode values of characters (similar to dictionary order).

Supported Operators:
--------------------
- `==`  : Equal to
- `!=`  : Not equal to
- `<`   : Less than
- `>`   : Greater than
- `<=`  : Less than or equal to
- `>=`  : Greater than or equal to

Examples:
---------
"a" < "b"          # True  → because Unicode of 'a' (97) < 'b' (98)
"apple" < "banana" # True  → 'a' < 'b'
"abc" == "abc"     # True
"abc" != "ABC"     # True  → case-sensitive
"Zoo" > "apple"    # False → 'Z' (90) < 'a' (97) in Unicode

Key Points:
-----------
- Comparisons are **case-sensitive** — uppercase letters come before lowercase.
- Longer strings are compared character-by-character from left to right.
- If one string is a prefix of another, the shorter string is considered smaller.

Example (prefix comparison):
----------------------------
"car" < "carpet"   # True → because "car" is a prefix of "carpet"

Use Cases:
----------
- Sorting strings alphabetically
- Validating input
- Creating conditional logic based on name or word order

Note:
-----
For case-insensitive comparisons, convert strings to the same case:
    name1.lower() == name2.lower()
"""

# Define two strings
str1 = "apple"
str2 = "banana"

# False (because "apple" is not equal to "banana")
print("str1 == str2 = ", str1 == str2)

# True  (because "apple" is different from "banana")
print("str1 != str2 = ", str1 != str2)

# False (because "apple" comes before "banana" in dictionary order)
print("str1 > str2  = ", str1 > str2)

# True  (because "apple" comes before "banana")
print("str1 < str2  = ", str1 < str2)

# Comparing Strings with Different Cases

# False ('A' has a smaller Unicode value than 'a')
print('"Apple" > "apple"   = ', "Apple" > "apple")
print('"apple" == "APPLE") = ', "apple" == "APPLE")  # False (case-sensitive)
print('"abc" < "abd"       = ', "abc" < "abd")      # True ('c' < 'd')

# Using Comparison Operators in an If Statement

word = "mango"
# Python compares strings lexicographically (like in a dictionary), based on Unicode values of characters — from left to right.
# Since "m" (109) is greater than "a" (97), Python considers "mango" > "apple".
# It doesn’t even need to look at the rest of the characters because the decision is made at the first differing character.


if word > "apple":
    print(f"{word} comes after apple in alphabetical order")
else:
    print(f"{word} comes before apple in alphabetical order")
