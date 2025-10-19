"""
__post_init__ for validation and derived fields

- Compute fields that depend on other fields
- Validate inputs after __init__ runs
"""

from dataclasses import dataclass


@dataclass
class TemperatureC:
    celsius: float
    fahrenheit: float = 0.0

    def __post_init__(self) -> None:
        self.fahrenheit = (self.celsius * 9 / 5) + 32


t = TemperatureC(25)
print("C:", t.celsius, "F:", t.fahrenheit)
