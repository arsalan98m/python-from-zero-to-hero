"""
isinstance() Function in Python
-------------------------------

The `isinstance()` function is used to determine whether a given object is an instance
of a specific class or a tuple of classes.

It returns:
- ✅ `True` → if the object is an instance (or subclass instance) of the given class(es)
- ❌ `False` → otherwise

Syntax:
-------
    isinstance(object, classinfo)

Parameters:
-----------
- `object`: The object you want to check.
- `classinfo`: A class, type, or a tuple of classes/types to check against.

Examples:
---------
x = 10
print(isinstance(x, int))        # True

y = "Hello"
print(isinstance(y, str))        # True

print(isinstance(y, (int, str))) # True (matches one of the types in the tuple)

z = [1, 2, 3]
print(isinstance(z, list))       # True
print(isinstance(z, dict))       # False

Use Cases:
----------
- Useful for type-checking in conditional logic
- Helps in writing functions that behave differently based on input type
- Commonly used in polymorphism and dynamic type validation

Notes:
------
- Also returns `True` if the object is an instance of a **subclass** of `classinfo`
- More Pythonic than using `type(obj) == SomeType` for inheritance-aware checks

"""

age: int = 20
weight: float = 65.5

print("check: isinstance(age, int)      = ", isinstance(age, int))  # True
print("check: isinstance(weight, int)   = ", isinstance(weight, int))  # False
print("check: isinstance(weight, float) = ", isinstance(weight, float))  # True
