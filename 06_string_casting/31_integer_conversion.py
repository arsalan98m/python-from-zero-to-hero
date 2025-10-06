# Integer Conversion

"""
Integer Conversion using int()
------------------------------

The `int()` function in Python is used to convert other data types into integers.

Supported Conversions:
----------------------
- Float → Integer
- String (if it represents a valid number) → Integer
- Boolean → Integer (`True` becomes 1, `False` becomes 0)

✅ Example 1: Float → Integer (Removes Decimal Part)
----------------------------------------------------
x = int(9.8)
print(x)  # Output: 9

🔹 Note:
- `int()` **truncates** the decimal part — it does **not** round.
    int(3.9) → 3  ✅ (not 4)

✅ Example 2: String → Integer
------------------------------
valid_str = "42"
print(int(valid_str))  # Output: 42

🔸 If the string is not a valid number, it raises a ValueError:
    int("hello")  # ❌ ValueError: invalid literal for int()

✅ Example 3: Boolean → Integer
-------------------------------
print(int(True))   # Output: 1
print(int(False))  # Output: 0

Use Cases:
----------
- Converting user input to integers
- Cleaning numeric data from text fields
- Logic-based toggles using boolean values

"""

# ✅ Example 1: Float → Integer (Removes Decimal Part)
#  Note: int() truncates (removes) the decimal part, it does not round.

num_float: float = 9.8
# skipped type hint to see what data type is assigned at runtime
num_int = int(num_float)
print(num_int, type(num_int))


# ✅ Example 2: String → Integer (Only Valid Numbers)
# ❌ Invalid Case: "123abc" cannot be converted to int(). It will raise a ValueError.

num_str = "123"
# num_str = "123abc" # Raises a ValueError

num_int = int(num_str)
print(num_int, type(num_int))

# ✅ Example 3: Boolean → Integer
print(int(True))  # Output: 1
print(int(False))  # Output: 0
