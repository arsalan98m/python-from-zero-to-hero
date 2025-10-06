"""
🔄 Do Lists and Tuples Share the Same Methods?

Short Answer:
🚫 No. Tuples do not support all the methods that lists do, because tuples are immutable.

✅ What Methods Tuples Support?

- count()
- index()


❌ What Tuples Do NOT Support (But Lists Do):

Tuples do not support methods like:

- append()
- extend()
- insert()
- remove()
- pop()
- sort()
- reverse()
- clear()

These are list-only because they require the data to be mutable (changeable).
"""

fruits = ("apple", "banana", "cherry", "banana")

print("fruits[0]: ", fruits[0])  # apple
print("fruits[-1]: ", fruits[-1])  # banana

print("fruits.count('banana'): ", fruits.count("banana"))  # 2
print("fruits.index('banana'): ", fruits.index("banana"))  # 1

# ❌ This will raise ValueError: tuple.index(x): x not in tuple
print("fruits.index('orange'): ", fruits.index("orange"))
