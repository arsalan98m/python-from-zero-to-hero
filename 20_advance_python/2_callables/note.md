# Python Callables Tutorial

Welcome to the comprehensive Python Callables tutorial! 🚀

## Table of Contents

### 1. Introduction to Callables

- **File:** `1_intro_to_callables.py`
- **Topics:** What are callables, callable() function, types of callables, **call** method basics

### 2. The **call** Method

- **File:** `2_call_method.py`
- **Topics:**
  - Implementing **call**
  - Callables with parameters
  - Real-world examples: converters, validators, calculators
  - Stateful callables

### 3. Functions as First-Class Objects

- **File:** `3_function_objects.py`
- **Topics:**
  - Functions as variables
  - Functions in data structures
  - Functions as arguments (higher-order functions)
  - Returning functions
  - Closures

### 4. Decorators as Callables

- **File:** `4_decorators_as_callables.py`
- **Topics:**
  - Class-based decorators
  - Decorators with state
  - Parameterized decorators
  - Real examples: timers, counters, validators, caching

### 5. Practical Examples

- **File:** `5_practical_examples.py`
- **Topics:**
  - Event system with callbacks
  - Strategy pattern for payments
  - Query filters
  - Middleware pipeline
  - Command pattern

### 6. Advanced Callable Techniques

- **File:** `6_advanced_callables.py`
- **Topics:**
  - Partial application
  - Type checking
  - Lazy evaluation
  - Function composition
  - Data pipelines
  - Retry mechanisms
  - Chainable operations

## Quick Reference

### What is a Callable?

A callable is any object that can be called using parentheses `()`.

```python
# Check if something is callable
callable(function_name)  # True for functions
callable(42)            # False for numbers
```

### Types of Callables

1. **Functions**

   ```python
   def greet(name):
       return f"Hello, {name}!"
   ```

2. **Lambda functions**

   ```python
   square = lambda x: x ** 2
   ```

3. **Classes** (calling creates instances)

   ```python
   class Person:
       def __init__(self, name):
           self.name = name
   ```

4. **Methods**

   ```python
   class Calculator:
       def add(self, a, b):
           return a + b
   ```

5. **Objects with **call\*\*\*\*

   ```python
   class Multiplier:
       def __init__(self, factor):
           self.factor = factor

       def __call__(self, value):
           return value * self.factor
   ```

### Making Objects Callable

```python
class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return f"{self.greeting}, {name}!"

hello = Greeter("Hello")
print(hello("Alice"))  # "Hello, Alice!"
```

### Class-Based Decorators

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@CountCalls
def my_function():
    return "Hello"
```

## Common Use Cases

### 1. Callbacks (Event Handling)

```python
def on_click(button_id):
    print(f"Button {button_id} clicked")

button.on_click(on_click)  # Pass function as callback
```

### 2. Strategy Pattern

```python
class PaymentProcessor:
    def process(self, amount, strategy):
        return strategy(amount)

result = processor.process(100, credit_card_payment)
```

### 3. Validators

```python
class AgeValidator:
    def __init__(self, min_age):
        self.min_age = min_age

    def __call__(self, age):
        return age >= self.min_age

validate_adult = AgeValidator(18)
print(validate_adult(25))  # True
```

### 4. State Machines

```python
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count
```

### 5. Data Transformation

```python
class DataPipeline:
    def __init__(self, *transforms):
        self.transforms = transforms

    def __call__(self, data):
        for transform in self.transforms:
            data = transform(data)
        return data
```

## Benefits of Callables

✅ **Flexibility** - Pass behavior as objects
✅ **Encapsulation** - Bundle data with behavior
✅ **State Management** - Objects can maintain state between calls
✅ **Reusability** - Create configurable, reusable components
✅ **Clean APIs** - Intuitive function-like interfaces
✅ **Design Patterns** - Enable Strategy, Command, Factory patterns

## When to Use Callables

### Use **call** when:

- You need a function-like object with state
- Building configurable functions (validators, converters)
- Implementing decorators with state
- Creating factory functions
- Building pipelines or chains

### Use regular functions when:

- You don't need state between calls
- Simple, stateless operations
- One-time transformations

## Common Patterns

### Factory Pattern

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
```

### Strategy Pattern

```python
class Processor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, data):
        return self.strategy(data)
```

### Command Pattern

```python
class Command:
    def __call__(self):
        pass  # Execute command
```

### Decorator Pattern

```python
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Calling function")
        return self.func(*args, **kwargs)
```

## Running the Examples

Each file is self-contained and can be run independently:

```bash
python 1_intro_to_callables.py
python 2_call_method.py
python 3_function_objects.py
# ... and so on
```

## Best Practices

1. **Use callable() to check** if an object is callable before calling it
2. **Keep **call** focused** - one clear purpose per callable
3. **Document behavior** - explain what calling the object does
4. **Consider functools** - use functools.wraps for decorators
5. **State management** - be careful with mutable state in callables
6. **Error handling** - handle errors gracefully in **call**

## Common Pitfalls

❌ Forgetting that classes themselves are callable
❌ Not using functools.wraps in decorators
❌ Overusing **call** when a regular method would be clearer
❌ Mutable default arguments in callables
❌ Not checking if something is callable before calling

## Next Steps

1. Start with `1_intro_to_callables.py` to understand basics
2. Learn `2_call_method.py` for custom callable objects
3. Study `3_function_objects.py` for first-class functions
4. Master `4_decorators_as_callables.py` for advanced decorators
5. Review `5_practical_examples.py` for real-world patterns
6. Explore `6_advanced_callables.py` for advanced techniques

---

Happy Learning! 🎓
