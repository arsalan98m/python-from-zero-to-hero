"""
Pool of String Literals in Python
---------------------------------

In Python, a pool of string literals is a mechanism used by the interpreter
to manage memory efficiently by reusing immutable string objects.

How It Works:
-------------
When Python encounters a string literal, it follows these steps:

1. Interning:
   - Python checks if the string is already interned (i.e., previously stored in memory).
   - If yes, it reuses the existing string reference.

2. String Literal Pool:
   - If the string is not interned, Python checks a cache known as the string literal pool.
   - If the string is present in the pool, it reuses it.

3. Create New String:
   - If the string is not found in either the interned cache or the pool,
     Python creates a new string object and stores it.

Benefits:
---------
- Memory Efficiency:
  Reduces memory usage by avoiding duplicate string allocations.

- Performance:
  Improves performance by allowing faster string comparisons and access.

- Internalization:
  Common strings are internalized, enabling better optimization during runtime.

Note:
-----
- This optimization typically applies to simple strings and identifiers.
- Developers can manually intern strings using `sys.intern()` if needed.

Pronunciation:
- Cache is pronounced as "kash".
"""

a: str = "hello"
b: str = "hello"

# Both a and b refer to the same string object in memory.
print(id(a))
print(id(b))


c: str = a + ""  # Nothing happen because we are appending a empty string.
print(id(c))

d: str = a + " "  # A new string object is created in the pool.
print(id(d))
