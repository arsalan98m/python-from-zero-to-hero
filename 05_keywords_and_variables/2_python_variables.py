"""
Python Variables
----------------

In Python, variables are used to store data that can be referenced and manipulated during program execution.
A variable is essentially a name assigned to a value.

Unlike many other programming languages, Python does not require explicit type declarations.
The **type is inferred** from the value assigned.

Example:
---------
name = "Alice"     # String
age = 25           # Integer
price = 19.99      # Float

Variables act as placeholders for data, allowing values to be stored and reused throughout a program.

Naming Rules
------------
To define variables correctly in Python, follow these rules:

1. Variable names can include letters, digits, and underscores (_).
2. Variable names **must not begin with a digit**.
3. Variable names are **case-sensitive** (`myVar` and `myvar` are different).
4. Do **not use Python keywords** as variable names (e.g., `if`, `for`, `class`).

Valid Examples:
---------------
name = "Alice"
_age = 25
salary2024 = 50000
my_variable = "Python"

Invalid Examples:
-----------------
2name = "Bob"          # ❌ Starts with a digit
my-variable = "Error"  # ❌ Contains a hyphen
class = "CS101"        # ❌ Uses a reserved keyword
$a = 10               # ❌ Starts with a special character

Naming Conventions
------------------

+----------------------------+------------------------------+-------------------------+
| Convention                | Used For                     | Example                 |
+============================+==============================+=========================+
| snake_case                | Variables, functions         | total_price, user_name  |
| CamelCase / PascalCase    | Classes                      | BankAccount, MyModel    |
| UPPER_CASE                | Constants                    | PI, MAX_SPEED           |
| _single_leading_underscore| "Private" variables          | _config, _password      |
| __double_leading          | Name mangling (internal use) | __secret_key            |
| __dunder__                | Special methods              | __init__, __str__       |
+----------------------------+------------------------------+-------------------------+

Special Naming Use Cases
-------------------------

+----------------------+-----------------------------+-----------------------------+
| Type                 | Example                     | Purpose                     |
+======================+=============================+=============================+
| Regular Variable     | total_cost                  | General use                 |
| Constant             | PI = 3.14159                | Immutable values            |
| Class Name           | BankAccount                 | Class definitions           |
| Private Variable     | _password                   | Internal use (not enforced) |
| Name Mangling        | __secret_key                | Avoid overrides in subclass |
| Special Method       | __init__, __str__           | Built-in dunder methods     |
+----------------------+-----------------------------+-----------------------------+

Best Practices (PEP 8)
----------------------
- Use `snake_case` for variable and function names.
- Use `PascalCase` (CapWords) for class names.
- Use `UPPER_CASE` for constants.
- Prefix internal variables with a single underscore (`_`).
- Avoid using reserved keywords as variable names.

"""

# **** Assigning Different Values ****
# We can assign different values to multiple variables simultaneously, making the code concise and easier to read.

x, y, z = 1, 2.5, "Python"

print("x = ", x)
print("y = ", y)
print("z = ", z)

# Using type hints while assigning multiple variables simultaneously cause and error invalid syntax
# x: int, y: float, z: str = 1, 2.5, "Python"  # ❌ Invalid syntax

# ***** Delete a Variable Using del Keyword *****
# We can remove a variable from the namespace using the del keyword. This effectively deletes the variable and frees up the memory it was using.

x: int = 10
print("x = ", x)

del x
print("x = ", x)  # ❌ NameError: name 'x' is not defined
