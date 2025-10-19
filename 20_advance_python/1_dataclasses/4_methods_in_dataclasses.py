"""
Dataclasses can include regular methods

- Define behavior alongside data
- Methods can use and update fields
"""

from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    age: int

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def celebrate_birthday(self) -> None:
        self.age += 1


u = User("Aisha", "Khan", 21)
print(u.full_name())
u.celebrate_birthday()
print(u.age)
