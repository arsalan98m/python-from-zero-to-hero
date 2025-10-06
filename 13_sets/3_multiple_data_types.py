# 📌 It can hold multiple data types at once.

multi_type_set: set = {7, 9.0, False, True, "Hello, World!", (1, 5, 9, 'hi')}
print("multi_type_set = ", multi_type_set)

"""
📌 The set is unordered
Note that items in the set collection may not follow the same order in which they are entered.
The position of items is optimized by Python to perform operations over set as defined in mathematics.

Python sets are unordered collections, but internally, elements are stored based on their hash values.
However, this internal structure is not predictable or stable across operations"
"""

my_set: set = {'Java', 'Python', 'JavaScript', 'java'}
print(my_set)
