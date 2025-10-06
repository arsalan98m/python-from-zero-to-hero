"""
copy()

Returns a shallow copy of the set.

What it does:
- Creates a new set with the same elements as the original.
"""

original = {1, 2, 3}
copied = original.copy()
print(copied)  # Output: {1, 2, 3}

copied.add(4)
print(original)  # Output: {1, 2, 3}
print(copied)    # Output: {1, 2, 3, 4}
