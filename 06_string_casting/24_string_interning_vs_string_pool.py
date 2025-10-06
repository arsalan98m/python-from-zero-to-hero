"""
String Interning vs. String Literal Pool in Python
---------------------------------------------------

String interning and the string literal pool are closely related concepts in Python,
both aiming to optimize memory and improve performance when working with strings.
However, they are not exactly the same.

1. String Interning:
---------------------
String interning is a process where Python stores only one copy of a string
value in memory and reuses it for identical strings.

- When a string is interned, any variable assigned that exact string value will
  reference the same memory location.
- Interning happens automatically for:
    - Short strings
    - Identifiers (e.g., variable names)
    - Some compile-time constants
- You can manually intern strings using `sys.intern()` for performance optimization.

Example:
    import sys
    a = sys.intern("hello world")
    b = sys.intern("hello world")
    print(a is b)  # True

2. String Literal Pool:
------------------------
The string literal pool is an internal cache of string literals written
directly in the code.

- Python automatically places these literals in a shared memory pool.
- If two identical string literals are used in code, they will typically
  refer to the same object in memory.

Example:
    a = "python"
    b = "python"
    print(a is b)  # True

Key Differences:
----------------
| Feature     | String Interning                         | String Literal Pool                    |
|-------------|------------------------------------------|----------------------------------------|
| What it is  | A process of reusing identical strings   | A memory area holding string literals  |
| Scope       | Can apply to any string (manual/auto)    | Only applies to literals in code       |
| Usage       | Can use `sys.intern()` manually          | Handled automatically by Python        |
| Control     | Partially controlled by developer        | Fully managed by the interpreter       |

Notes:
------
- In Python, the pool and interning work together under the hood.
- Using `is` checks for memory reference equality.
- Using `==` checks for value equality.

Summary:
--------
While both terms refer to ways Python avoids creating duplicate string objects,
"interning" refers to **the act of reusing** string instances, whereas the
"string literal pool" refers to **where those interned strings may reside**.
"""
