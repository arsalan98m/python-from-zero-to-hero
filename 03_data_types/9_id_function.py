"""
id() Function in Python
------------------------

The `id()` function returns the unique identifier (memory address) of an object.
This identifier is guaranteed to be unique and constant for the object during its lifetime.

Syntax:
-------
id(object)

Returns:
--------
- An integer that represents the identity of the given object.

Purpose of id():
----------------
1. Identify Objects:
   - Every object in Python has a unique ID that can be accessed using `id()`.
   - This ID usually corresponds to the memory address where the object is stored.

2. Check Object Equality:
   - While `==` checks if two objects have the same value,
     `id()` can be used to check if two variables reference the **exact same object**.

3. Debugging:
   - Useful for tracking variables and object references during debugging.
   - Helps distinguish between objects with the same value but different identities.

Examples:
---------
a = [1, 2, 3]
b = a
c = [1, 2, 3]

id(a) == id(b)  # True → Both refer to the same object
id(a) == id(c)  # False → Same value, different objects

Notes:
------
- The ID is only guaranteed to be unique while the object exists.
- Once an object is garbage collected, its ID may be reused by a new object.

"""

x: str = None
y: str = None
z: str = x

print("ID of variable x  = " + str(id(x)))
print("ID of variable y  = " + str(id(y)))
print("ID of variable z  = " + str(id(z)))
print("\nIs variable x & y shares the same memory space? \nThe answer is: " +
      str(id(x) == id(y)))

"""
False in a boolean context: None is considered False in a boolean context, 
meaning that it can be used in conditional statements.
"""

if (None):
    print("if block")
else:
    print("else block")
