"""
Frozen (immutable) dataclasses

- Instances cannot be modified after creation
- Attempting to assign raises FrozenInstanceError
"""

from dataclasses import dataclass, FrozenInstanceError


@dataclass(frozen=True)
class Point:
    x: int
    y: int


p = Point(1, 2)
print(p)
try:
    p.x = 10
except FrozenInstanceError as e:
    print("Error:", type(e).__name__, str(e))
