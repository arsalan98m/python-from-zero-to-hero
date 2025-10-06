"""
global vs nonlocal in Python

Python provides two special keywords—`global` and `nonlocal`—to manage variable scope across different levels of functions.

1. global:
- Used to declare that a variable inside a function refers to the global scope.
- Allows modification of a variable defined outside all functions.
- Commonly used when functions need to update global variables.

2. nonlocal:
- Used in nested (inner) functions to refer to variables in the nearest enclosing (non-global) scope.
- Enables modification of a variable defined in the outer function.
- Useful for maintaining state or updating values in closures.

Scope Behavior:
- `global` affects variables in the module-level/global scope.
- `nonlocal` affects variables in the closest enclosing function scope, excluding the global scope.

Use Case:
- Use `global` when updating a truly global variable.
- Use `nonlocal` when working inside nested functions and modifying outer (but not global) variables.
"""


chai_type = "ginger"


def update_order():
    chai_type = "Elaichi"

    def kitchen():
        # After this line, chai_type is no longer local, it's now enclosing scope
        nonlocal chai_type
        chai_type = "Kesar"

    kitchen()
    print(f"After kitchen update: {chai_type}")


update_order()
