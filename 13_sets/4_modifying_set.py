"""
The set can not be Change Directly using [ ]

When we say that set items are unchangeable, it means that you cannot modify an individual item in a set directly.
However, you can add or remove items from the set.

- set's are unordered, so indexing doesn't work my_set[0]
- set object does not support item assignment my_set[0] = 10
"""

# Creating a set
my_set: set = {1, 2, 3, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}

my_set[0] = 10  # ❌ TypeError: 'set' object does not support item assignment
