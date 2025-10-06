"""
4. Assignment Operators in Python
----------------------------------

Assignment operators are used to assign or update the value of a variable.

They can perform basic arithmetic operations and directly update the variable in a compact form.

Operator Summary:
-----------------

| Operator | Example   | Equivalent To  | Description                         |
|----------|-----------|----------------|-------------------------------------|
| `=`      | x = 5     | x = 5          | Assigns the value 5 to variable `x` |
| `+=`     | x += 3    | x = x + 3      | Adds 3 to the current value of `x`  |
| `-=`     | x -= 3    | x = x - 3      | Subtracts 3 from `x`                |
| `*=`     | x *= 3    | x = x * 3      | Multiplies `x` by 3                 |
| `/=`     | x /= 3    | x = x / 3      | Divides `x` by 3 (returns float)    |
| `//=`    | x //= 3   | x = x // 3     | Floor divides `x` by 3              |

Example:
--------
x = 10
x += 5     # x becomes 15
x *= 2     # x becomes 30
x //= 4    # x becomes 7

These operators simplify code and are especially useful in loops or calculations involving repeated updates.
"""
x = 5
print("Assignment: x = 5                    ", x)  # Output: 5

x += 3  # Equivalent to x = x + 3
print("Addition Assignment: x += 3          ", x)  # Output: 8

x -= 3  # Equivalent to x = x - 3
print("Subtraction Assignment: x -= 3       ", x)  # Output: 5

x *= 3  # Equivalent to x = x * 3
print("Multiplication Assignment: x *= 3    ", x)  # Output: 15

x /= 3  # Equivalent to x = x / 3
print("Division Assignment: x /= 3          ", x)  # Output: 5.0

x //= 3  # Equivalent to x = x // 3
print("Floor Division Assignment: x //= 3   ", x)  # Output: 1.0
