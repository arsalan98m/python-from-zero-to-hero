"""
Sequence Types in Python
-------------------------

Sequence types are ordered collections of elements that support:
- Indexing
- Slicing
- Iteration
- Membership testing
- Length retrieval using len()

Python provides several built-in sequence types:

1️⃣ list
---------
- A mutable, ordered sequence of items.
- Elements can be added, removed, or changed.
- Can contain items of mixed data types.

2️⃣ tuple
----------
- An immutable, ordered sequence.
- Once created, the elements cannot be modified.
- Often used for fixed collections of data (e.g., coordinates).

3️⃣ str (string)
----------------
- A sequence of Unicode characters.
- Immutable and supports powerful string operations.
- Useful for storing and manipulating text.

4️⃣ range
----------
- Represents an immutable sequence of numbers.
- Commonly used in loops and iteration.
- Defined by start, stop, and step values.

Why Sequences Matter:
---------------------
- They provide a uniform way to store and work with multiple items.
- Built-in methods and syntax make data manipulation easy and consistent.
- Understanding sequences is foundational for mastering Python data structures.

"""

# a. String (str)
# A sequence of characters enclosed in quotes.


text_double: str = "Hello, Python!"  # Strings with Double Quotes ("")
text_single: str = 'Hello, Python!'  # Strings with Single Quotes ('')
text_multi: str = '''Hello, Python!'''  # Multi-Line Strings with Triple Quotes (''' ''' or """ """)
text_multi_1: str = """Hello, Python!"""  # Multi-Line Strings with Triple Quotes (''' ''' or """ """)

print(type(text_double), "text_double = ", text_double)
print(type(text_single), "text_single = ", text_single)
print(type(text_multi), "text_multi = ", text_multi)
print(type(text_multi_1), "text_multi_1 = ", text_multi_1)

"""
Key Takeaways
- Double Quotes ("): Use when the string contains single quotes.
- Single Quotes ('): Use when the string contains double quotes.
- Triple Quotes (''' or \"""): Use for multi-line strings or doc-strings.
"""

# b. List (list)
# An ordered, mutable collection.

# Type hinting is not enforced in python, but you should mention appropriate data type in this case 'list'
my_list: list = [1, 2, 3, "Python", 3.14, 3+2j]
print(type(my_list), " my_list = " + str(my_list))

# c. Tuple (tuple)
# An ordered, immutable collection.
my_tuple: tuple = (1, 2, 3, "AI", 2.71, False, .3, 3+2j)
print(type(my_tuple), " my_tuple = ", my_tuple)

# d. Range (range)
# Represents a sequence of numbers.
num_range: range = range(1, 10, 2)  # range(start, stop, step)
print(type(num_range), " num_range = ", num_range.step)
