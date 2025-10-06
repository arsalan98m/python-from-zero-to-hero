"""
discard(elem)

Removes the specified element if it exists. If not, it does nothing

What it does:
- Safe alternative to remove() if you're unsure the element exists.

Summary:
remove() method:

- The remove() method removes the specified item from the set.
- If the item is not found in the set, it raises a KeyError.
- This method is suitable when you are sure that the item exists in the set.

discard() method:

- The discard() method also removes the specified item from the set.
- However, if the item is not found in the set, it does not raise any error. It simply does nothing.
- This method is suitable when you are not sure if the item exists in the set.
"""

my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print("my_set = ", my_set)

# discard() only removes a single element.
# {1, 2, 3} is a set itself, not an element within my_set.
# Therefore, discard does not find it and returns None, without modifying the set.
print(my_set.discard({1, 2, 3}))

print("After: my_set = ", my_set)  # return None

# To remove multiple elements, iterate and discard each one individually:
for item in {1, 2, 3}:
    my_set.discard(item)

print("After removing multiple elements: my_set = ", my_set)
