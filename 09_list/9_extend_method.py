
"""
extend() Method
The .extend() method adds multiple elements from another list (or any iterable) to the end of the list.
"""
fruits: list = ["apple", "banana", "cherry"]

another_fruits: list = ["mango", "pineapple"]

print("Before extending: ", fruits)

# It add the elements of another_fruits at the end of the fruits list and return None
fruits.extend(another_fruits)  # this modify the original list

print("After extending: ", fruits)
