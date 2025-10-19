"""
Dataclass inheritance

- Subclasses extend fields from base dataclasses
"""

from dataclasses import dataclass


@dataclass
class Entity:
    id: int


@dataclass
class User(Entity):
    name: str
    age: int


u = User(1, "Ali", 25)
print(u)
