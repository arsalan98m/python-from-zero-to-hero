"""
remove() Method in Python Lists
===============================

The `remove()` method is used to delete the first occurrence of a specified value from a list.

or

The .remove(value) method deletes the first matching value. Raises ValueError if the value is not found.

Key Aspects:

- Value-based:
  Searches for a specific value and removes its first occurrence.

- Returns None:
  The method does not return any value; it modifies the list in place.

- Raises ValueError:
  If the specified value is not found in the list, a ValueError is raised.

Commonly used when you know the exact value you want to remove from the list.

"""

fruits: list = ["apple", "banana", "cherry", "banana"]

print("Before removing: ", fruits)

# Removes 'banana' # run multiple times to see error as "banana" is already removed
fruits.remove("banana")
fruits.remove("banana")
# fruits.remove("banana")  # ❌ ValueError: list.remove(x): x not in list
# fruits.remove("abid")  # ❌ ValueError: list.remove(x): x not in list
# fruits.remove() # ❌ TypeError: remove() takes exactly one argument (0 given)

print("After removing: ", fruits)
