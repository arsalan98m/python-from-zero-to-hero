"""
pop() Method in Python Lists
============================

The `pop()` method is used to remove and return an item at a specified index from a list.
If no index is provided, it removes and returns the last item.

or 

The .pop(index) method removes and returns the element at the given index. If no index is provided, removes the last item.

Key Aspects:

- Index-based:
  Removes the element at the given index. Defaults to the last item if no index is specified.

- Returns the removed item:
  Unlike `remove()`, `pop()` returns the item it removes from the list.

- Raises IndexError:
  If the specified index is out of range, an IndexError exception is raised.

Useful when the position of the item is known and its value is needed after removal.

"""

fruits: list = ["apple", "banana", "cherry"]

# Removes and returns the element at index 1 # run it multiple time to see error
deleted_fruit = fruits.pop(1)  # this modify the original list

print("deleted element = ", deleted_fruit)  # Output: 'banana'

fruits.pop()  # this will remove the last element

# fruits.pop(1)  # ❌ this will raise IndexError: pop index out of range

print(fruits)  # Output: ['apple' ]
