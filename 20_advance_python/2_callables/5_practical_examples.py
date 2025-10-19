"""
Practical uses of callables

- Strategy dispatch with callable values
- Sorted key functions
- Simple validation pipeline
"""

from typing import Callable, Dict, Iterable, List


def add(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


strategies: Dict[str, Callable[[int, int], int]] = {
    "add": add,
    "mul": mul,
}

print("strategy add:", strategies["add"](2, 3))
print("strategy mul:", strategies["mul"](2, 3))


words = ["masala", "chai", "ginger", "karak"]
print(sorted(words, key=len))


Validator = Callable[[str], bool]


def is_not_empty(s: str) -> bool:
    return bool(s.strip())


def is_lower(s: str) -> bool:
    return s == s.lower()


def validate(value: str, validators: Iterable[Validator]) -> List[bool]:
    return [v(value) for v in validators]


print(validate("chai", [is_not_empty, is_lower]))
print(validate(" Chai ", [is_not_empty, is_lower]))
