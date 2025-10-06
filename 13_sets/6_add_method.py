"""
add(elem)

Adds a single, immutable element to the set.

What it does:
- If the element doesn't already exist in the set, it will be added.
- If it does, the set remains unchanged.
"""

my_set = {1, 2, 3}
my_set.add(4)

print(my_set)  # Output: {1, 2, 3, 4}

my_set.add(2)
print(my_set)  # Output: {1, 2, 3, 4}
