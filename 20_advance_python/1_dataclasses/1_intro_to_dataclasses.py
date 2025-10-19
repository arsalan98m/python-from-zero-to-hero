"""
Dataclasses: a concise way to create classes that store data

Key features
- Auto-generated __init__, __repr__, __eq__ by default
- Type annotations define fields
- Optional features: defaults, ordering, immutability, post-init hooks

Run this file to see the default __repr__ and field access in action.
"""

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


person = Person("Ali", 30)
print(person)              # e.g., Person(name='Ali', age=30)
print(person.name, person.age)
