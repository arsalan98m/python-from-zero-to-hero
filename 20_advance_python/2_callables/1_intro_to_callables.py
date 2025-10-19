"""
Intro to callables

- In Python, anything you can call like f() is a callable
- Functions, lambdas, and objects implementing __call__ are callables
- Use built-in callable(obj) to check
"""


def add(a: int, b: int) -> int:
    return a + b


def adder(x, y): return x + y  # noqa: E731 (simple lambda for demo)


class Greeter:
    def __init__(self, name: str) -> None:
        self.name = name


class GreeterCallable:
    def __init__(self, name: str) -> None:
        self.name = name

    def __call__(self, who: str) -> str:
        return f"{self.name} says hello to {who}"


print("callable(add):", callable(add))
print("callable(adder):", callable(adder))
# classes are callable to construct
print("callable(Greeter):", callable(Greeter))
print("callable(Greeter() instance):", callable(Greeter("Ali")))
print("callable(GreeterCallable):", callable(GreeterCallable))
print("callable(GreeterCallable() instance):",
      callable(GreeterCallable("Sara")))

g = GreeterCallable("Aisha")
print(g("World"))
