"""
Basic dataclass usage

- Fields are declared with type hints
- __init__, __repr__, and __eq__ are generated automatically
- Two instances with the same field values are equal
"""

from dataclasses import dataclass


@dataclass
class Car:
    make: str
    model: str
    year: int


car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Toyota", "Corolla", 2020)
car3 = Car("Toyota", "Camry", 2020)

print(car1)
print("car1 == car2:", car1 == car2)
print("car1 == car3:", car1 == car3)
