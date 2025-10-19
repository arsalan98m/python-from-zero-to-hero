"""
Decorators are callables that return callables

- Function-based decorator
- Class-based decorator using __call__
"""

from functools import wraps
from time import perf_counter


def log_calls(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__} with", args, kwargs)
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} returned", result)
        return result
    return wrapper


@log_calls
def add(a: int, b: int) -> int:
    return a + b


class Timer:
    def __init__(self, fn):
        wraps(fn)(self)
        self._fn = fn

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        result = self._fn(*args, **kwargs)
        end = perf_counter()
        print(f"{self._fn.__name__} took {end - start:.6f}s")
        return result


@Timer
def slow_add(a: int, b: int) -> int:
    total = 0
    for _ in range(1_0000):
        total += 1
    return a + b + total * 0


print(add(2, 3))
print(slow_add(2, 3))
