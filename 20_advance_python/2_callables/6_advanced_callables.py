"""
Advanced callable patterns

- Partial application
- Closures capturing state
"""

from functools import partial


def power(base: int, exp: int) -> int:
    return base ** exp


square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(4))
print(cube(3))


def make_multiplier(factor: int):
    def mul(x: int) -> int:
        return x * factor
    return mul


times10 = make_multiplier(10)
print(times10(7))
