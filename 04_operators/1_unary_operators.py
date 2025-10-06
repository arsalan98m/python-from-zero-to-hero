"""
Operators and Operands in Python
--------------------------------

In Python (and programming in general), an **operand** is the value or variable that an **operator** acts upon.

Definitions:
------------
- **Operator**: A symbol that performs an operation (e.g., `+`, `-`, `*`, `/`)
- **Operand**: The data (values or variables) that the operator uses

Examples:
    In the expression `a + b`:
    - `+` is the operator
    - `a` and `b` are operands

Key Concepts:
-------------
1️⃣ Unary Operators
--------------------
- Work with **one operand**
- Perform operations on a single value

Examples:
---------
1. **Negative (-)**: Changes the sign
    x = 5
    y = -x  # y becomes -5

2. **Logical NOT (`not`)**: Reverses a boolean
    a = True
    b = not a  # b becomes False

3. **Bitwise NOT (`~`)**: Inverts binary bits
    x = 5            # Binary:  0101
    y = ~x           # Result: -6 (two's complement)
    bin(x)           # '0b101'
    format(x, 'b')   # '101'

2️⃣ Binary Operators
---------------------
- Work with **two operands**
- Perform operations between two values

Examples:
---------
1. **Arithmetic**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
2. **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
3. **Logical**: `and`, `or`
4. **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`, etc.
5. **Bitwise**: `&`, `|`, `^`, `<<`, `>>`

Key Difference:
---------------
- **Unary Operators**: Work with ONE operand (e.g., `-x`, `not x`, `~x`)
- **Binary Operators**: Work with TWO operands (e.g., `a + b`, `x > y`, `x and y`)

Note:
-----
You can use the `bin()` function to display an integer in binary form:
    x = 5
    print(bin(x))         # '0b101'
    print(format(x, 'b')) # '101'

We'll explore each category of operator in more detail in upcoming sections.
"""

# 1. Unary Operators
# Unary operators work with one operand (a single value or variable). They perform operations on just one thing.

# 1.1. Negative (-)
x = 5
y = -x  # y is now -5
print("y =", y)


# 1.2. Logical NOT (`not`)
a = True
b = not a  # b becomes False because a is True
print("b =", b)
