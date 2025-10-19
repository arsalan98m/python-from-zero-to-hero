"""
Defaults with dataclasses

- Use normal Python defaults for simple types
- Use default_factory for mutable defaults (like list, dict, set)
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Student:
    name: str
    grade: int = 1
    tags: List[str] = field(default_factory=list)  # safe mutable default


s1 = Student("Sara")
s2 = Student("Sara")

s1.tags.append("honor")

print(s1)
print(s2)
print("s1.tags is s2.tags:", s1.tags is s2.tags)  # False, separate lists
