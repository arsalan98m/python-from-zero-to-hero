"""
Intro to Generics (typing)

- Use TypeVar to write type-safe reusable functions
- Helps static checkers understand relationships between inputs and outputs
"""

from typing import Iterable, List, TypeVar


T = TypeVar("T")


def to_list(items: Iterable[T]) -> List[T]:
    return list(items)


print(to_list({1, 2, 3}))
print(to_list(("chai", "coffee")))
