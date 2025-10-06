"""
Integer Literals in Python
---------------------------

An **integer literal** is a sequence of digits used to represent a whole number (integer)
in Python source code. These literals can be assigned to variables and used in expressions.

Examples of integer literals:
-----------------------------
- Decimal:      10, 42, -7
- Binary:       0b1010       (prefix with 0b)
- Octal:        0o17         (prefix with 0o)
- Hexadecimal:  0x1A         (prefix with 0x)

Memory Space Sharing (Integer Interning):
-----------------------------------------
In Python, small integer literals (usually between -5 and 256) are **interned** —
meaning they are stored in a shared memory space and reused to save memory and
improve performance.

This means that assigning the same small integer literal to multiple variables
does not create separate objects in memory — they all point to the same location.

Example:
--------
x = 100
y = 100
z = 100

print(id(x), id(y), id(z))      # All IDs will be the same
print(x is y is z)              # True

However:
--------
a = 1000
b = 1000
print(a is b)   # May be False (no guarantee of interning for large integers)

Use Cases:
----------
- Useful for optimization when working with frequently used small integers.
- Helps understand Python's memory model and object identity.

Note:
-----
- `is` checks if two variables reference the same object in memory.
- `==` checks if two variables have the same value (regardless of identity).

"""

# Note: For better results, use this code inside google colab or jupyter notebook

x: int = 1
y: int = 1
z: int = x

# Note: when you need to concatenate any thing with string you need to first cast it to str()
print("Value of x = " + str(x) + ", and id(x) = " + str(id(x)))
print("Value of y = " + str(y) + ", and id(y) = " + str(id(y)))
print("Value of z = " + str(z) + ", and id(z) = " + str(id(z)))

print("id(x) == id(y) = ", id(x) == id(y))  # True
print("id(x) is id(y) = ", id(x) is id(y))  # False

print("\n ===================== \n")

# Integer Interning
x = -6
y = -6
z = x

print("Value of x = " + str(x) + ", and id(x) = " + str(id(x)))
print("Value of y = " + str(y) + ", and id(y) = " + str(id(y)))
print("Value of z = " + str(z) + ", and id(z) = " + str(id(z)))

print("\n ===================== \n")

a = 257
b = 257
c = a

print("Value of a = " + str(a) + ", and id(a) = " + str(id(a)))
print("Value of b = " + str(b) + ", and id(b) = " + str(id(b)))
print("Value of c = " + str(c) + ", and id(c) = " + str(id(c)))
