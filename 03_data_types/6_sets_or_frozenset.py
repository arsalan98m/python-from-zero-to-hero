"""
Set Types

Unordered collections with unique elements.

a. Set (set)
Mutable, unordered, and contains unique values.

b. Frozen Set (frozenset)
Immutable version of a set.
"""

# a. Set (set)
my_set: set = {1, 2, 33, 4, 4, 5}
print(type(my_set), "my_set = ", my_set)


# b. Frozen Set (frozenset)
frozen_set: frozenset = frozenset([1, 2, 3, 4, 4, 5])
print(type(frozen_set), "frozen_set = ", frozen_set)
