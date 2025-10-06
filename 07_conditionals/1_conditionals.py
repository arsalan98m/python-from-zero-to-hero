"""
1. Introduction to Control Flow
-------------------------------
Control flow determines the order in which instructions are executed in a program.
In Python, this is handled using conditional statements like `if`, `elif`, and `else`,
in combination with comparison and logical operators.

2. Comparison Operators
------------------------
Comparison operators are used to compare values and evaluate expressions that return
Boolean results (`True` or `False`).

- `==` : Equal to
- `!=` : Not equal to
- `>`  : Greater than
- `<`  : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

3. Logical Operators
---------------------
Logical operators allow combining multiple conditions:

- `and` : Returns `True` if both conditions are true.
- `or`  : Returns `True` if at least one condition is true.
- `not` : Reverses the result of the condition.

4. The if Statement
--------------------
The `if` statement executes a block of code only when a specified condition evaluates to `True`.

5. The else Statement
----------------------
The `else` block executes if the `if` condition evaluates to `False`.

6. The elif Statement
----------------------
The `elif` (else if) block lets you check multiple expressions for `True`, one after the other.

7. Nested if Statements
-------------------------
An `if` statement placed inside another `if` block is called a nested if. It allows checking
more complex conditional logic.

8. Practical Use Cases
-----------------------
- Building decision trees
- Conditional calculations
- Menu-based logic systems
- Validating user inputs

Summary:
--------
- Use `if` for a single condition.
- Use `if...else` for binary decisions.
- Use `if...elif...else` for multiple branching conditions.
- Use nested `if` blocks for more complex logic.
- Combine conditions with logical operators (`and`, `or`, `not`).

"""

# Example  (Comparison Operators)
x: int = 10
y: int = 20

print("x == y = ", x == y)  # False
print("x != y = ", x != y)  # True
print("x > y  = ", x > y)   # False
print("x < y  = ", x < y)   # True
print("x >= y = ", x >= y)  # False
print("x <= y = ", x <= y)  # True
