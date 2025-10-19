"""
TypeVar basics

- Constrain TypeVar to a set of types
- The same T is preserved across parameters and return
"""

from typing import TypeVar


Number = TypeVar("Number", int, float)


def average(a: Number, b: Number) -> float:
    return (a + b) / 2


print(average(2, 4))
print(average(2.0, 4.0))
