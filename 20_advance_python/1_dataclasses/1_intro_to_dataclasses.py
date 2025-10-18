"""
Introduction to Dataclasses
===========================

What are Dataclasses?
- Introduced in Python 3.7
- A decorator that automatically generates special methods for classes
- Reduces boilerplate code
- Makes code cleaner and more readable

Why use Dataclasses?
- Automatic __init__() method generation
- Automatic __repr__() method generation
- Automatic __eq__() method generation
- Less code to write and maintain
- Clear intent that the class is primarily for storing data
"""

# Traditional way of creating a class (WITHOUT dataclass)
from dataclasses import dataclass


class PersonTraditional:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"PersonTraditional(name={self.name!r}, age={self.age!r}, city={self.city!r})"

    def __eq__(self, other):
        if not isinstance(other, PersonTraditional):
            return False
        return (self.name, self.age, self.city) == (other.name, other.age, other.city)


# Modern way using dataclass (WITH dataclass)


@dataclass
class PersonModern:
    name: str
    age: int
    city: str


# Usage comparison
print("=" * 60)
print("Traditional Class:")
print("=" * 60)
person1 = PersonTraditional("Alice", 30, "New York")
print(person1)  # Uses custom __repr__
print(f"Name: {person1.name}")
print()

print("=" * 60)
print("Dataclass (Much cleaner!):")
print("=" * 60)
person2 = PersonModern("Alice", 30, "New York")
print(person2)  # Automatically has __repr__
print(f"Name: {person2.name}")
print()

# Comparison works automatically
print("=" * 60)
print("Equality Comparison:")
print("=" * 60)
person3 = PersonModern("Alice", 30, "New York")
person4 = PersonModern("Bob", 25, "Boston")

print(f"person2 == person3: {person2 == person3}")  # True (same values)
print(f"person2 == person4: {person2 == person4}")  # False (different values)
print()

# Code saved: Instead of ~15 lines of boilerplate, we only need 4 lines!
print("=" * 60)
print("Lines of Code Comparison:")
print("=" * 60)
print("Traditional class: ~15 lines")
print("Dataclass: 4 lines")
print("Time saved: A LOT! 🚀")
