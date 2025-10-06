# ********** String Repetition **********

"""
String Repetition in Python
----------------------------

String repetition is a simple and efficient way to create a new string
by repeating an existing string multiple times using the `*` operator.

The Basics:
-----------
- You multiply a string by an integer.
- This produces a new string that repeats the original string the specified number of times.

Examples:
---------
"abc" * 3
# Output: 'abcabcabc'

"Python! " * 2
# Output: 'Python! Python! '

Key Points:
-----------
- The `*` operator must be used with an integer on the right-hand side.
- Multiplying a string by `0` results in an empty string `""`.
- Repetition is non-destructive — the original string remains unchanged.

Use Cases:
----------
- Creating visual separators:
    print("-" * 30)
    # Output: ------------------------------

- Generating repeating patterns:
    print("AB" * 5)
    # Output: ABABABABAB

- Building test data or dummy output:
    repeated = "test " * 4
    # Output: 'test test test test '

Note:
-----
- If a negative integer is used, the result is also an empty string.
- Works with all string types, including whitespace and symbols.

"""

base_string = "Hello"
repetition_count = 3

repeated_string = base_string * repetition_count

print(f"Original string: {base_string}")
print(f"Repeated string: {repeated_string}")

# Using repetition for visual separators
separator = "-" * 30
print(separator)

# Repeating with different strings and counts
pattern = "* "
repeated_pattern = pattern * 5
print(repeated_pattern)

# Repeating zero times
empty_string = "Test" * 0
print(f"Empty string: '{empty_string}'")

# using string repetition in a loop.
for i in range(1, 6):
    print("*"*i)

# if a negative integer is used, the result is also an empty string.
empty_string = "Test" * -10
print(f"Empty string: '{empty_string}'")
