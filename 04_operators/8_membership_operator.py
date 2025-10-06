"""
Membership Operators in Python
------------------------------

Used to check if a value exists within a sequence (like list, tuple, set, string, or dictionary).

+------------+-----------------------------------------------+------------------+
| Operator   | Description                                   | Example          |
+============+===============================================+==================+
| in         | Returns True if the value is present          | x in my_list     |
|            | in the sequence                               |                  |
+------------+-----------------------------------------------+------------------+
| not in     | Returns True if the value is NOT present      | x not in my_list |
|            | in the sequence                               |                  |
+------------+-----------------------------------------------+------------------+

Examples:
----------
my_list = [1, 2, 3]

2 in my_list       # True
4 not in my_list   # True
5 in my_list       # False
"""


my_list: list = [1, 2, 3, 4, 5]

print("my_list           = ", my_list)            # [1, 2, 3, 4, 5]
print("3 in my_list      = ", 3 in my_list)       # True
print("10 not in my_list = ", 10 not in my_list)  # True

print("\n-----\n")

my_string: str = "Test user"
print("'T' in my_string          = ", 'T' in my_string)         # True
print("'Hello' not in my_string  = ", 'Hello' not in my_string)  # True
