"""
Sets in Python
==============

A set is one of Python's 4 built-in data types for storing collections of data.
The others are: List, Tuple, and Dictionary — each with different behavior and use cases.

What is a Set?
--------------
- A set is an **unordered**, **unindexed**, and **mutable** collection.
- It does **not allow duplicate elements**.
- Useful for **membership tests**, **removing duplicates**, and performing **mathematical set operations**.

Key Characteristics:
--------------------
1. **Unordered**: Items have no defined order, and the order can change.
2. **Unindexed**: Items cannot be accessed via an index (e.g., set[0] is invalid).
3. **Mutable**: Items can be added or removed after the set is created.
4. **Unique Elements**: Duplicate values are automatically removed.

Common Uses:
------------
- Removing duplicates from a list
- Checking if an item exists
- Performing set algebra: 
  - `union()` → Combine elements
  - `intersection()` → Common elements
  - `difference()` → Items only in one set
  - `symmetric_difference()` → Items in either set but not both

Creation:
---------
- Use curly braces: `my_set = {1, 2, 3}`
- Or use the constructor: `my_set = set([1, 2, 3])`
- To create an **empty set**, use `set()` instead of `{}`, because `{}` creates an empty dictionary.

Example:
--------
>>> my_set = {1, 2, 3, 2}
>>> print(my_set) 
{1, 2, 3}  # Duplicate 2 is automatically removed
"""


# 📌 Creating a Set
my_set: set = {123, 452, 5, 6}

# 📌 Creating a Set using set()
my_set2: set = set([123, 452, 5, 6])

# 📌 Creating a Set using {}
unknown: set = {}  # set or dictionary

# 📌 Creating an empty Set
empty_set: set = set()


print("my_set            = ", my_set)  # {123, 452, 5, 6}
print("my_set2           = ", my_set2)  # {123, 452, 5, 6}
print("type(my_set)      = ", type(my_set))  # <class 'set'>
print("type(my_set2)     = ", type(my_set2))  # <class 'set'>
print("type(unknown)     = ", type(unknown))  # <class 'dict'>
print("type(empty_set)   = ", type(empty_set))  # <class 'set'>
print("my_set == my_set2 = ", my_set == my_set2)  # True
