"""
Type Casting in Python
-----------------------

Type casting refers to the process of converting a value from one data type to another.

Python supports two primary forms of type casting:

1️⃣ Implicit Type Casting
--------------------------
- Python automatically converts one data type to another when it makes sense to do so.
- This usually happens in expressions involving mixed data types (e.g., int and float).

Example:
    x = 5        # int
    y = 2.5      # float
    result = x + y  # x is implicitly converted to float
    # result = 7.5 (float)

2️⃣ Explicit Type Casting
--------------------------
- You can manually convert values from one type to another using built-in functions.

Common casting functions:
    - `int()`   → Converts to integer (truncates float, parses valid numeric strings)
    - `float()` → Converts to float
    - `str()`   → Converts to string
    - `bool()`  → Converts to boolean (non-zero or non-empty → True)

Examples:
    a = int("10")        # → 10
    b = float(5)         # → 5.0
    c = str(3.14)        # → '3.14'
    d = bool(0)          # → False

Why Type Casting Matters:
--------------------------
- Ensures proper operations between different data types
- Prevents runtime type errors
- Helps when interacting with user input (which is often string-based)

"""


# Integer variable
age: int = 10
print("Age = " + str(age) + ", Type = " + str(type(age)))

# Float variable
price: float = 20.5

# Implicit type casting: int + float = float
total_amount: float = age + price
print("Total amount = " + str(total_amount) +
      ", Type = " + str(type(total_amount)))

# Another float value
temperature: float = 66.89
print("Temperature = " + str(temperature) +
      ", Type = " + str(type(temperature)))

# Explicit type casting: float to int (decimal is truncated)
rounded_temp: int = int(temperature)
print("Rounded temperature = " + str(rounded_temp) +
      ", Type = " + str(type(rounded_temp)))

# String representation a float
user_input: str = "25.8"

# Convert string to float
converted_float: float = float(user_input)
print("Converted float = " + str(converted_float) +
      ", Type = " + str(type(converted_float)))

# ❌ Error example: string to int directly (not allowed for "25.8")
# converted_int: int(user_input) # ❌ Value Error

# corrected by converting string → float → int
converted_int: int = int(float(user_input))
print("Converted int = " + str(converted_int) +
      ", Type = " + str(type(converted_int)))
