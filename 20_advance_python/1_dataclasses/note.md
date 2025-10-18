# Python Dataclasses Tutorial

Welcome to the comprehensive Python Dataclasses tutorial! 🚀

## Table of Contents

### 1. Introduction

- **File:** `1_intro_to_dataclasses.py`
- **Topics:** What are dataclasses, why use them, basic comparison with traditional classes

### 2. Basic Dataclass

- **File:** `2_basic_dataclass.py`
- **Topics:** Creating simple dataclasses, real-world examples (Book, Product, Student, Location)

### 3. Default Values

- **File:** `3_default_values.py`
- **Topics:** Setting default values, Optional fields, field ordering rules

### 4. Methods in Dataclasses

- **File:** `4_methods_in_dataclasses.py`
- **Topics:** Adding custom methods, combining data with behavior

### 5. Field Function

- **File:** `5_field_function.py`
- **Topics:**
  - `default_factory` for mutable defaults
  - `repr`, `compare`, `init` parameters
  - Field metadata

### 6. Post-Init Processing

- **File:** `6_post_init.py`
- **Topics:** `__post_init__` method, validation, computed fields

### 7. Frozen Dataclasses

- **File:** `7_frozen_dataclasses.py`
- **Topics:** Immutability with `frozen=True`, hashable objects, when to use frozen

### 8. Ordering and Comparison

- **File:** `8_ordering_and_comparison.py`
- **Topics:** `order=True`, sorting, comparison operators, min/max

### 9. Inheritance

- **File:** `9_inheritance.py`
- **Topics:** Class inheritance, method overriding, polymorphism, abstract base classes

### 10. Real-World Example

- **File:** `10_real_world_example.py`
- **Topics:** Complete e-commerce system demonstrating all concepts together

## Quick Reference

### Basic Dataclass Syntax

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = ""  # default value
```

### Common Parameters

```python
@dataclass(
    frozen=True,    # Make immutable
    order=True,     # Add comparison methods
)
class Example:
    field1: str
```

### Field Options

```python
from dataclasses import dataclass, field

@dataclass
class Example:
    # Mutable default
    items: list = field(default_factory=list)

    # Don't show in repr
    password: str = field(repr=False)

    # Don't use in comparison
    timestamp: str = field(compare=False)

    # Don't include in __init__
    computed: int = field(init=False)
```

### Post-Init Processing

```python
@dataclass
class Example:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height
```

## Key Benefits of Dataclasses

1. ✅ **Less Boilerplate Code** - Automatic generation of special methods
2. ✅ **Type Hints** - Built-in support for type annotations
3. ✅ **Readable** - Clear intent that class is for storing data
4. ✅ **Flexible** - Can add methods, validation, computed fields
5. ✅ **Immutable Option** - `frozen=True` for immutable objects
6. ✅ **Comparison Support** - `order=True` for sorting

## When to Use Dataclasses

✅ Use dataclasses when:

- You need to store related data together
- You want automatic `__init__`, `__repr__`, `__eq__` methods
- You need simple data containers with type hints
- Building configuration objects, DTOs, value objects

❌ Don't use dataclasses when:

- You need a simple dictionary
- Your class is primarily behavior-focused (few attributes)
- You're working with Python < 3.7

## Running the Examples

Each file is self-contained and can be run independently:

```bash
python 1_intro_to_dataclasses.py
python 2_basic_dataclass.py
# ... and so on
```

## Next Steps

1. Start with `1_intro_to_dataclasses.py` to understand the basics
2. Progress through files 2-9 to learn specific features
3. Study `10_real_world_example.py` to see everything combined
4. Experiment with your own examples!

---

Happy Learning! 🎓
