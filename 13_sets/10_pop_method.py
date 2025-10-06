"""
pop()

Removes and returns an arbitrary element from the set.

What it does:
- Because sets are unordered, the popped element is random.
- Raises KeyError if the set is empty.
"""

my_set = {10, 20, 30}
item = my_set.pop()

print(item)     # Output: Could be 10 or 20 or 30
print(my_set)   # Output: Remaining elements

empty = set()
# empty.pop()  # ❌ Raises KeyError
