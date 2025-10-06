"""
Ternary Operator in Python
===========================

A ternary operator in Python provides a way to write conditional expressions in a single line.
It evaluates a condition and returns one of two values depending on whether the condition is
True or False.

Syntax:
--------
<value_if_true> if <condition> else <value_if_false>

Use Case:
---------
Ternary operators are useful for simple decisions, like assigning a value based on a condition
without writing a full if-else block.
"""

# Example: Ternary Operator
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
