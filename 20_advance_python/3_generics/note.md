# Python Generics Tutorial

Welcome to the comprehensive Python Generics tutorial! 🚀

## Table of Contents

### 1. Introduction to Generics

- **File:** `1_intro_to_generics.py`
- **Topics:** What are generics, why use them, TypeVar basics, comparing with/without generics

### 2. TypeVar Basics

- **File:** `2_typevar_basics.py`
- **Topics:**
  - Creating TypeVars
  - Single and multiple TypeVars
  - Type preservation
  - Naming conventions

### 3. Generic Classes

- **File:** `3_generic_classes.py`
- **Topics:**
  - Generic[T] base class
  - Stack, Queue, Box containers
  - Multiple type parameters
  - Repository pattern
  - Result types

### 4. Bounded TypeVars

- **File:** `4_bounded_typevars.py`
- **Topics:**
  - Constraining type variables
  - Bounded by class hierarchy
  - Protocols for duck typing
  - Comparable types
  - Number operations

### 5. Real-World Examples

- **File:** `5_real_world_examples.py`
- **Topics:**
  - API response wrappers
  - Repository pattern
  - Observable pattern
  - Builder pattern
  - State machines
  - Validator chains

## Quick Reference

### What are Generics?

Generics allow you to write code that works with multiple types while maintaining type safety. They're like templates that work with any type.

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

def get_first(items: List[T]) -> T:
    return items[0]

# Type is inferred!
num = get_first([1, 2, 3])  # Type: int
text = get_first(["a", "b"])  # Type: str
```

### Creating TypeVars

```python
from typing import TypeVar

# Basic TypeVar (any type)
T = TypeVar('T')

# Multiple TypeVars
T = TypeVar('T')
U = TypeVar('U')
K = TypeVar('K')  # Key
V = TypeVar('V')  # Value

# Bounded TypeVar (only specific types)
NumericType = TypeVar('NumericType', int, float)

# Bounded by class
from numbers import Number
NumType = TypeVar('NumType', bound=Number)
```

### Generic Functions

```python
from typing import TypeVar, List

T = TypeVar('T')

def reverse(items: List[T]) -> List[T]:
    """Reverse a list while preserving type"""
    return items[::-1]

# Usage
nums = reverse([1, 2, 3])  # Type: List[int]
words = reverse(["a", "b"])  # Type: List[str]
```

### Generic Classes

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

# Usage
int_stack: Stack[int] = Stack()
str_stack: Stack[str] = Stack()
```

### Multiple Type Parameters

```python
from typing import TypeVar, Generic

K = TypeVar('K')
V = TypeVar('V')

class Pair(Generic[K, V]):
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value

# Usage
pair: Pair[str, int] = Pair("age", 30)
```

### Bounded TypeVars

```python
from typing import TypeVar

# Only allow specific types
StringOrBytes = TypeVar('StringOrBytes', str, bytes)

def length(data: StringOrBytes) -> int:
    return len(data)

# Bounded by base class
class Animal:
    pass

AnimalType = TypeVar('AnimalType', bound=Animal)

def feed(animal: AnimalType) -> None:
    # Works with Animal and all subclasses
    pass
```

## Common Patterns

### 1. Container Classes

```python
class Container(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get_all(self) -> List[T]:
        return self.items
```

### 2. Repository Pattern

```python
class Repository(Generic[T]):
    def __init__(self):
        self.storage: Dict[int, T] = {}

    def save(self, item: T) -> None:
        self.storage[id(item)] = item

    def find_all(self) -> List[T]:
        return list(self.storage.values())
```

### 3. Result Type

```python
class Result(Generic[T]):
    def __init__(self, value: Optional[T] = None,
                 error: Optional[str] = None):
        self.value = value
        self.error = error

    def is_success(self) -> bool:
        return self.error is None
```

### 4. Builder Pattern

```python
class Builder(Generic[T]):
    def __init__(self, factory: Callable[[], T]):
        self.factory = factory
        self.actions: List[Callable[[T], None]] = []

    def with_action(self, action) -> 'Builder[T]':
        self.actions.append(action)
        return self

    def build(self) -> T:
        obj = self.factory()
        for action in self.actions:
            action(obj)
        return obj
```

## Benefits of Generics

✅ **Type Safety** - Catch errors at development time
✅ **Code Reusability** - One implementation for many types
✅ **Better IDE Support** - Autocomplete knows exact types
✅ **Self-Documenting** - Clear what types are expected
✅ **Refactoring Safety** - Type checker helps during changes
✅ **No Runtime Overhead** - Type hints are removed at runtime

## When to Use Generics

### Use Generics when:

- Building container classes (Stack, Queue, List)
- Creating utility functions that work with any type
- Implementing design patterns (Repository, Builder, Factory)
- Building APIs that work with user-defined types
- You want to preserve type information through operations
- Creating reusable library code

### Don't use Generics when:

- Function only works with one specific type
- Type doesn't matter (like logging)
- Adding unnecessary complexity
- You're not using type checkers

## Type Checker Tools

Python type checkers that understand generics:

- **mypy** - Most popular, standalone
- **pyright** - Fast, used by VS Code
- **pyre** - Facebook's type checker
- **pytype** - Google's type checker

```bash
# Install and run mypy
pip install mypy
mypy your_file.py
```

## Common TypeVar Names

| Name     | Usage                                |
| -------- | ------------------------------------ |
| `T`      | Generic type (most common)           |
| `U`, `V` | Additional generic types             |
| `K`      | Key type (for dicts)                 |
| `V`      | Value type (for dicts)               |
| `E`      | Element type                         |
| `R`      | Return type                          |
| `Self`   | Type of current class (Python 3.11+) |

## Protocols vs Abstract Base Classes

### Protocol (Duck Typing)

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

# Any class with draw() method matches!
```

### Abstract Base Class

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

# Must explicitly inherit from Shape
```

## Advanced Features

### Generic Type Aliases

```python
from typing import TypeVar, List, Dict

T = TypeVar('T')

# Create type aliases
Vector = List[T]
Matrix = List[List[T]]
Cache = Dict[str, T]
```

### Covariance and Contravariance

```python
# Covariant (can return subtypes)
T_co = TypeVar('T_co', covariant=True)

# Contravariant (can accept supertypes)
T_contra = TypeVar('T_contra', contravariant=True)
```

## Best Practices

1. **Use meaningful names** - Prefer `ItemType` over just `T` when it adds clarity
2. **Keep it simple** - Don't over-complicate with too many type parameters
3. **Document bounds** - Explain why TypeVar is bounded
4. **Use Protocols** - For duck typing and interface requirements
5. **Type hints are optional** - Don't feel forced to use them everywhere
6. **Run type checkers** - Actually use mypy or pyright to get benefits

## Common Pitfalls

❌ Forgetting Generic[T] base class for generic classes
❌ Using mutable default values in generic classes
❌ Not understanding covariance/contravariance
❌ Over-constraining TypeVars unnecessarily
❌ Mixing runtime type checking with static typing
❌ Not running a type checker to verify annotations

## Running the Examples

Each file is self-contained and can be run independently:

```bash
cd 23_generics
python 1_intro_to_generics.py
python 2_typevar_basics.py
# ... and so on
```

To run type checking:

```bash
pip install mypy
mypy 1_intro_to_generics.py
```

## Python Version Requirements

- **Python 3.5+**: Basic type hints (`List[int]`, `Dict[str, int]`)
- **Python 3.6+**: Variable annotations (`x: int = 5`)
- **Python 3.7+**: `from __future__ import annotations`
- **Python 3.9+**: Built-in generics (`list[int]` instead of `List[int]`)
- **Python 3.10+**: Union types (`int | str` instead of `Union[int, str]`)
- **Python 3.11+**: `Self` type, Exception Groups
- **Python 3.12+**: Generic type parameter syntax

## Next Steps

1. Start with `1_intro_to_generics.py` for fundamentals
2. Learn `2_typevar_basics.py` for TypeVar usage
3. Master `3_generic_classes.py` for building containers
4. Study `4_bounded_typevars.py` for constraints
5. Review `5_real_world_examples.py` for practical patterns
6. Install mypy and practice type checking
7. Apply generics to your own projects

## Resources

- [PEP 484](https://www.python.org/dev/peps/pep-0484/) - Type Hints
- [PEP 585](https://www.python.org/dev/peps/pep-0585/) - Built-in Generics
- [mypy documentation](https://mypy.readthedocs.io/)
- [typing module docs](https://docs.python.org/3/library/typing.html)

---

Happy Learning! 🎓

