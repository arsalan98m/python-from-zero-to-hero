"""
insert() Method

The .insert(index, item) method inserts an item at the specified index, shifting the rest to the right.

both index and item are required
"""

fruits: list = ["apple", "banana", "cherry"]

print("Before inserting: ", fruits)

fruits.insert(1, "orange")  # insert at index 1
# fruits.insert(100, "orange")  # this will insert item on the last of the list

print("After inserting: ", fruits)
