"""
append() Method
The .append() method adds a single element to the end of the list.
"""

fruits: list = ["apple", "banana", "cherry"]

print("Before appending: ", fruits)

# It add the element at the end of the list and return None
fruits.append("orange")  # this modify the original list

print("After appending: ", fruits)
