"""
update(iterable)

Adds multiple elements to the set from any iterable (list, tuple, another set, etc.).

What it does:
- Updates the set with elements from the provided iterable. Duplicates are ignored.
"""

my_set = {1, 2}
my_set.update([1, 2, 3, 4])
print(my_set)  # {1, 2, 3, 4}

# my_set.update(5)  # ❌ TypeError: 'int' object is not iterable
