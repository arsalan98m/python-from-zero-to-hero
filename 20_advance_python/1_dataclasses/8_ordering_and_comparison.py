"""
Ordering support (order=True)

- Dataclasses can generate rich comparisons for sorting
"""

from dataclasses import dataclass


@dataclass(order=True)
class Score:
    points: int
    name: str


scores = [
    Score(90, "Ali"),
    Score(75, "Sara"),
    Score(90, "Zain"),
    Score(100, "Aisha"),
]

print("Original:", scores)
print("Sorted:", sorted(scores))
