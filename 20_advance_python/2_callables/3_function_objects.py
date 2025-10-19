"""
Functions are objects

- You can store them in variables, lists, dicts
- You can pass them to other functions (higher-order functions)
- You can even attach attributes to them
"""

from typing import Callable, List


def greet(name: str) -> str:
    return f"Hello, {name}!"


def apply_twice(fn: Callable[[int], int], x: int) -> int:
    return fn(fn(x))


def increment(n: int) -> int:
    return n + 1


funcs: List[Callable[[str], str]] = [greet, str.upper]
print([f("chai") for f in funcs])

print(apply_twice(increment, 3))

# Attaching an attribute to a function
greet.times_called = 0  # type: ignore[attr-defined]
print("greet attribute set:", hasattr(greet, "times_called"))
