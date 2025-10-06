"""
Truthy and Falsy Values in Python (Boolean Context)
---------------------------------------------------

In Python, values can be evaluated in a boolean context — such as in conditions (`if`, `while`, etc.).
These values are classified as either:

- ✅ Truthy → Evaluated as `True`
- ❌ Falsy  → Evaluated as `False`

You do not need to explicitly convert values to `True` or `False` — Python does it automatically.

Truthy Values:
--------------
These values are considered `True` when evaluated in a boolean context:

- Non-zero integers (e.g., 1, -5, 42)
- Non-empty strings (e.g., "hello", "0")
- Non-empty lists (e.g., [1], ['a'])
- Non-empty tuples (e.g., (1,))
- Non-empty dictionaries (e.g., {"key": "value"})
- Non-empty sets (e.g., {10, 20})

Falsy Values:
-------------
These values are considered `False`:

- Zero (`0`, `0.0`, `-0`, `-0.0`)
- Empty string (`""`)
- Empty list (`[]`)
- Empty tuple (`()`)
- Empty dictionary (`{}`)
- Empty set (`set()`)
- `None`
- `False` (the boolean value itself)

Examples:
---------
if []:
    print("This is truthy")
else:
    print("This is falsy")  # This will be printed

if "Python":
    print("This is truthy")  # This will be printed

Use Case:
---------
Understanding truthy and falsy values helps in writing clean conditional checks without explicit comparisons.

Instead of:
    if len(my_list) != 0:
        ...

You can write:
    if my_list:
        ...
"""
k: int = -9  # Any number either positive or negative, beside '0' or '-0' ZERO is considered True
b: bool = bool(k)
print(f"b = {b} and type of b = {type(b)}")

if (k):
    print("k is truthy")
else:
    print("k is falsy")


print('check: bool("55") = ', bool("55"))  # True
print('check: bool("") = ', bool(""))  # False
print('check: bool([]) = ', bool([]))  # False
print('check: bool([1, 2, 3]) = ', bool([1, 2, 3]))  # True
print('check: bool({}) = ', bool({}))  # False
print('check: bool({"name":"abid}) = ', bool({"name": "abid"}))  # False
