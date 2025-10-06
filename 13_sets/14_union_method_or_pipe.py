"""
Using the union() method or | operator:

Union: Returns all elements from both sets but in unique form

In Python, the union() method or the | operator is used to combine two sets into a single set. This operation
returns a new set containing all unique elements from both sets.

Using the union() method:
The union() method is a built-in method of the set data type in Python. It takes an iterable (such as a set, list, or
tuple) as an argument and returns a new set containing all unique elements from both the original set and the iterable.

Key aspects of union() and | operator:

- Unique elements: The resulting set contains only unique elements from both sets.
- Order does not matter: The order in which the sets are combined does not affect the result.
- Original sets remain unchanged: The original sets are not modified by the union operation.
"""

my_set: set = {1, 2, 3, 5}
my_set_2: set = {1, 5, 6, 7}

my_set3: set = my_set.union(my_set_2)
# my_set3: set = my_set | my_set_2
print(my_set3)  # {1, 2, 3, 5, 6, 7}
