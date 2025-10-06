"""
remove(elem)

Removes the specified element from the set.

What it does:
- If the element exists in the set, it will be removed.
- If it does not, it will raise a KeyError.
"""

my_set = {1, 2, 3}
my_set.remove(2)  # Output: None

print(my_set)  # {1, 3}

# my_set.remove(5)  # ❌ Raises KeyError: 5 not in set
