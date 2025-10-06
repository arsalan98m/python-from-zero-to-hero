"""
3. Logical Operators in Python
-------------------------------

Logical operators are used to combine or invert boolean expressions (conditions).

They return `True` or `False` based on the logic between the expressions.

Operator Summary:
-----------------

| Operator | Name         | Description                            | Example                     | Result |
|----------|--------------|----------------------------------------|-----------------------------|--------|
| `and`    | Logical AND  | Returns True if both conditions are True | (5 > 3 and 10 > 5)         | True   |
| `or`     | Logical OR   | Returns True if at least one condition is True | (5 > 3 or 10 < 5)   | True   |
| `not`    | Logical NOT  | Reverses the boolean value              | not(5 > 3)                  | False  |

Examples:
---------
a = 5
b = 10

# AND
print(a > 3 and b > 5)   # True

# OR
print(a > 3 or b < 2)    # True

# NOT
print(not (a < b))       # False

Use Case:
---------
Logical operators are commonly used in:
- `if` statements
- loops
- combining multiple comparisons (with `and`, `or`)
- inverting a condition (with `not`)
"""

x: bool = True
y: bool = False

print("x and y", x and y)  # False
print("x or y", x or y)  # False
print("not x", not x)  # False
