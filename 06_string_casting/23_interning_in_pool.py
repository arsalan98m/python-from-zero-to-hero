"""
Interning in Python
-------------------

1. What is Interning?
---------------------
Interning is a memory optimization technique where Python stores only one copy
of certain immutable strings in memory and reuses it whenever the same string
is used again. This helps reduce memory usage and improves performance,
especially during string comparisons.

2. Which Strings Are Interned?
------------------------------
- Short Strings:
  Python typically interns short strings (usually 20 characters or fewer).

- Identifiers:
  Strings that resemble valid variable names (e.g., "x", "count", "my_var")
  are automatically interned by Python.

- Explicit Interning:
  You can manually intern any string using the `sys.intern()` function from
  the `sys` module.

Example:
--------
```python
import sys

a = sys.intern("hello_world")
b = sys.intern("hello_world")

print(a is b)  # True, both point to the same memory location
"""


import sys
a = sys.intern("hello world!")
b = sys.intern("hello world!")
print(a is b)  # True (manually interned)

print(id(a))
print(id(b))
