"""
Tuples in Python

A tuple is an `ordered`, `immutable` (unchangeable) sequence of elements.
Tuples are useful for fixed data collections.
"""

# 📌 Example 1: Creating a tuple with different data types
fruits = ("apple", "banana", "cherry")
print("fruits: ", fruits)

# 📌 Example 2: Creating a number tuple
numbers = (1, 2, 3)
print("numbers: ", numbers)

# 📌 Example 3: Creating a tuple with multiple elements
multiple_elements = ("hello", 42, 3.14, True)
print("multiple_elements: ", multiple_elements)

# 📌 Example 4: Creating an empty tuple
empty_tuple = ()
print("empty_tuple: ", empty_tuple)


"""
Even though tuples are immutable, Python may create new instances in memory when you define 
identical tuples in separate assignments. This is why id(tuple_1) and id(tuple_2) may differ.

"""
tuple_1: tuple = (10, 20, 30)  # tuple
tuple_2: tuple = (10, 20, 30)  # tuple

print("id(tuple_1) = ", id(tuple_1))  # unique memory address
print("id(tuple_2) = ", id(tuple_2))  # unique memory address

print("tuple_1 == tuple_2 = ", tuple_1 == tuple_2)  # comparing by value

# 📌 Updating tuple is not allowed
# ❌ This will raise TypeError: 'tuple' object does not support item assignment
# tuple_1[0] = 100
