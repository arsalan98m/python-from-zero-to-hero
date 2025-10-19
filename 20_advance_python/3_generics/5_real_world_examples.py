"""
Real-world style generics

- Generic cache
- Generic result type (success/error)
"""

from dataclasses import dataclass
from typing import Dict, Generic, Optional, TypeVar


K = TypeVar("K")
V = TypeVar("V")


class SimpleCache(Generic[K, V]):
    def __init__(self) -> None:
        self._store: Dict[K, V] = {}

    def set(self, key: K, value: V) -> None:
        self._store[key] = value

    def get(self, key: K) -> Optional[V]:
        return self._store.get(key)


cache: SimpleCache[str, int] = SimpleCache()
cache.set("visits", 10)
print(cache.get("visits"))


T = TypeVar("T")
E = TypeVar("E")


@dataclass
class Ok(Generic[T]):
    value: T


@dataclass
class Err(Generic[E]):
    error: E


def divide(a: float, b: float) -> Ok[float] | Err[str]:
    if b == 0:
        return Err("division by zero")
    return Ok(a / b)


print(divide(10, 2))
print(divide(1, 0))
