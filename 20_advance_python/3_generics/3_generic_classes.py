"""
Generic classes

- Parameterize classes over types using typing.Generic
"""

from typing import Generic, Iterable, List, TypeVar


T = TypeVar("T")


class Bag(Generic[T]):
    def __init__(self, items: Iterable[T] = ()) -> None:
        self._items: List[T] = list(items)

    def add(self, item: T) -> None:
        self._items.append(item)

    def items(self) -> List[T]:
        return list(self._items)


ints = Bag[int]([1, 2, 3])
ints.add(4)
print(ints.items())

strings = Bag[str](["masala", "ginger"])
strings.add("karak")
print(strings.items())
