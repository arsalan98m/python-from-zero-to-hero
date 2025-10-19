"""
Bounded TypeVars

- Restrict T to subtypes of a bound
"""

from typing import Protocol, TypeVar


class SupportsArea(Protocol):
    def area(self) -> float: ...


TShape = TypeVar("TShape", bound=SupportsArea)


def total_area(a: TShape, b: TShape) -> float:
    return a.area() + b.area()


class Rect:
    def __init__(self, w: float, h: float) -> None:
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h


class Circle:
    def __init__(self, r: float) -> None:
        self.r = r

    def area(self) -> float:
        return 3.14159 * self.r * self.r


print(total_area(Rect(3, 4), Rect(2, 5)))
print(total_area(Circle(2), Circle(3)))
