# ********** Type Casting **********

"""
Comprehensive Guide to Type Casting in Python 🚀
------------------------------------------------

What is Type Casting?
----------------------
Type casting (also known as type conversion) is the process of converting one
data type into another. In Python, this is essential when combining or working
with different data types such as integers, floats, and strings.

Python supports two kinds of type casting:

1️⃣ Implicit Type Casting (Automatic Conversion)
------------------------------------------------
- Python automatically converts one data type to another **without user intervention**.
- This usually occurs when no data loss is expected.

Example:
    x = 10       # int
    y = 3.5      # float
    result = x + y
    print(result)        # Output: 13.5
    print(type(result))  # Output: <class 'float'>

In this case, Python implicitly converted `x` (int) to `10.0` (float)
so that both operands match the higher-precision `float` type.

Key Point:
----------
- Implicit casting is **safe** and **automatic**, ensuring precision is preserved.

2️⃣ Explicit Type Casting (Manual Conversion)
---------------------------------------------
- Explicit type casting is performed **manually** by the programmer using
  Python's built-in functions.
- It is useful when you need to convert data types intentionally — especially
  when working with user input, strings, or arithmetic operations between
  incompatible types.

Common Built-in Functions:
---------------------------
- `int()`    → Converts to integer
- `float()`  → Converts to floating-point number
- `complex()` → Converts to complex number
- `str()`    → Converts to string
- `bool()`   → Converts to boolean (True/False)
- `list()`   → Converts to list
- `tuple()`  → Converts to tuple
- `set()`    → Converts to set
- `dict()`   → Converts to dictionary


Examples:
---------
# Convert float to int
x = int(3.9)
print(x)  # Output: 3

# Convert int to string
y = str(25)
print(y)        # Output: '25'
print(type(y))  # Output: <class 'str'>

# Convert string to float
z = float("3.14")
print(z)  # Output: 3.14

# Convert value to boolean
print(bool(0))     # Output: False
print(bool("Hi"))  # Output: True

Key Point:
----------
- Be cautious: Explicit casting can lead to **data loss** (e.g., truncating decimals).
- Always validate the input before casting (especially when casting from strings).

"""

# ✅ Implicit Type Casting (Automatic Conversion)

# # Integer + Float → Result is automatically converted to float

a = 10  # int
b = 2.5  # float
result = a+b

print(result, type(result))

# ✅ Explicit Type Casting (Manual Conversion)

# ✅ Convert float to int
x = 9.8
converted_x = int(x)
print(converted_x, type(converted_x))

# ✅ Convert int to string
age = 30
age_str = str(age)
print(age_str, type(age_str))

# ✅ Convert string to float
price = "100.50"
converted_price = float(price)
print(converted_price, type(converted_price))

# converted_price = int(price)  # Raises an error in runtime because price is a float and int() cannot convert float to int


# ✅ Convert string to int (valid only if string contains a number)
num_str = "123"
converted_num = int(num_str)
print(converted_num, type(converted_num))

# ⚠️ Example that causes an error:
# invalid_str = "abc"
# int(invalid_str)  # Raises an error in runtime

# ⚠️ No Implicit Conversion Between str and int
num_str = "123"
num_int = 5
# print(num_str + num_int)  # Raises an error in runtime
