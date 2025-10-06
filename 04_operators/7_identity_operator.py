"""
Identity Operators in Python
----------------------------

Used to compare whether two variables refer to the same object in memory.

+-----------+-----------------------------+-------------------------+
| Operator  | Description                 | Example                 |
+===========+=============================+=========================+
| is        | Returns True if both        | x is y                  |
|           | variables point to the      |                         |
|           | same memory location        |                         |
+-----------+-----------------------------+-------------------------+
| is not    | Returns True if both        | x is not y              |
|           | variables point to different|                         |
|           | memory locations            |                         |
+-----------+-----------------------------+-------------------------+

Examples:
----------
x = [1, 2, 3]
y = x
z = [1, 2, 3]

x is y       # True  (same object)
x is z       # False (different objects, even though contents are equal)
x is not z   # True
"""

a: list = [1, 2, 3]
b: list = [1, 2, 3]
c: list = a

print("a is c", a is c)  # True (same object, sharing same memory space)
print("a is b", a is b)  # False (different objects, separate memory space)
# True (same values, different memory space but having same values)
print("a == b", a == b)
# True (different objects, separate memory space)
print("a is not b", a is not b)

print("\n -------- \n")

print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"id(c) = {id(c)}")
