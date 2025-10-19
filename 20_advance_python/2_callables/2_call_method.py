"""
Implementing __call__

- Objects with __call__ behave like functions
- Useful for stateful behaviors
"""


class Counter:
    def __init__(self, start: int = 0) -> None:
        self.count = start

    def __call__(self) -> int:
        self.count += 1
        return self.count


c = Counter()
print(c())
print(c())
print(c())
