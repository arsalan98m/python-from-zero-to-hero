"""
Advanced Callable Techniques
============================

Advanced patterns and techniques with callables
"""

from typing import Callable, TypeVar, Generic
import inspect


# Example 1: Partial Application (Creating specialized functions)
class Partial:
    """Manual implementation of functools.partial"""

    def __init__(self, func: Callable, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        # Combine stored and new arguments
        all_args = self.args + args
        all_kwargs = {**self.kwargs, **kwargs}
        return self.func(*all_args, **all_kwargs)


print("=" * 60)
print("Example 1: Partial Application")
print("=" * 60)


def multiply(a, b, c):
    return a * b * c


# Create specialized version
double_and_multiply = Partial(multiply, 2)
print(f"double_and_multiply(3, 4) = {double_and_multiply(3, 4)}")  # 2*3*4

triple_by_5 = Partial(multiply, 3, 5)
print(f"triple_by_5(2) = {triple_by_5(2)}")  # 3*5*2
print()


# Example 2: Callable with type checking
class TypedCallable:
    """Callable that enforces type checking"""

    def __init__(self, func: Callable, *arg_types):
        self.func = func
        self.arg_types = arg_types

    def __call__(self, *args):
        # Check argument types
        for arg, expected_type in zip(args, self.arg_types):
            if not isinstance(arg, expected_type):
                raise TypeError(
                    f"Expected {expected_type.__name__}, "
                    f"got {type(arg).__name__}"
                )
        return self.func(*args)


print("=" * 60)
print("Example 2: Type-Checked Callable")
print("=" * 60)


def add(a, b):
    return a + b


# Create type-checked version
typed_add = TypedCallable(add, int, int)

try:
    print(f"typed_add(5, 10) = {typed_add(5, 10)}")
    print(f"typed_add(5, 'hello') = {typed_add(5, 'hello')}")  # Error
except TypeError as e:
    print(f"Error: {e}")
print()


# Example 3: Lazy Evaluation
class Lazy:
    """Defer computation until result is needed"""

    def __init__(self, func: Callable):
        self.func = func
        self.result = None
        self.computed = False

    def __call__(self):
        if not self.computed:
            print("  Computing result...")
            self.result = self.func()
            self.computed = True
        else:
            print("  Using cached result...")
        return self.result


print("=" * 60)
print("Example 3: Lazy Evaluation")
print("=" * 60)


def expensive_computation():
    """Simulate expensive operation"""
    import time
    time.sleep(0.5)
    return sum(range(1000000))


lazy_result = Lazy(expensive_computation)

print("First call:")
value1 = lazy_result()
print(f"Result: {value1}")

print("\nSecond call:")
value2 = lazy_result()
print(f"Result: {value2}")
print()


# Example 4: Compose functions
class Compose:
    """Compose multiple functions: f(g(h(x)))"""

    def __init__(self, *functions):
        self.functions = functions

    def __call__(self, x):
        result = x
        # Apply functions in reverse order
        for func in reversed(self.functions):
            result = func(result)
        return result


print("=" * 60)
print("Example 4: Function Composition")
print("=" * 60)


def add_five(x):
    return x + 5


def multiply_by_two(x):
    return x * 2


def square(x):
    return x ** 2


# Compose: square(multiply_by_two(add_five(x)))
composed = Compose(square, multiply_by_two, add_five)

print(f"Input: 3")
print(f"add_five: 3 + 5 = 8")
print(f"multiply_by_two: 8 * 2 = 16")
print(f"square: 16² = 256")
print(f"composed(3) = {composed(3)}")
print()


# Example 5: Pipeline for data transformation
class Pipeline:
    """Chain transformations on data"""

    def __init__(self, *steps):
        self.steps = steps

    def __call__(self, data):
        result = data
        for step in self.steps:
            result = step(result)
        return result

    def add_step(self, step):
        """Add a new step to pipeline"""
        self.steps = self.steps + (step,)
        return self


print("=" * 60)
print("Example 5: Data Pipeline")
print("=" * 60)

# Transform text data


def remove_spaces(text):
    return text.replace(" ", "")


def to_uppercase(text):
    return text.upper()


def add_brackets(text):
    return f"[{text}]"


pipeline = Pipeline(remove_spaces, to_uppercase, add_brackets)

text = "hello world"
result = pipeline(text)
print(f"Input: '{text}'")
print(f"Output: '{result}'")
print()


# Example 6: Retry mechanism
class Retry:
    """Retry failed function calls"""

    def __init__(self, max_attempts: int = 3, delay: float = 0):
        self.max_attempts = max_attempts
        self.delay = delay

    def __call__(self, func: Callable):
        def wrapper(*args, **kwargs):
            import time

            for attempt in range(1, self.max_attempts + 1):
                try:
                    print(f"  Attempt {attempt}/{self.max_attempts}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  Failed: {e}")
                    if attempt == self.max_attempts:
                        print("  Max attempts reached, giving up")
                        raise
                    if self.delay > 0:
                        time.sleep(self.delay)

        return wrapper


print("=" * 60)
print("Example 6: Retry Mechanism")
print("=" * 60)

call_count = 0


@Retry(max_attempts=3, delay=0.1)
def unreliable_function():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("Connection failed")
    return "Success!"


try:
    result = unreliable_function()
    print(f"Result: {result}")
except Exception as e:
    print(f"Final error: {e}")
print()


# Example 7: Chainable operations
class ChainableList:
    """List with chainable operations using callables"""

    def __init__(self, data):
        self.data = list(data)

    def filter(self, predicate: Callable) -> 'ChainableList':
        """Filter elements"""
        self.data = [x for x in self.data if predicate(x)]
        return self

    def map(self, transform: Callable) -> 'ChainableList':
        """Transform elements"""
        self.data = [transform(x) for x in self.data]
        return self

    def reduce(self, reducer: Callable, initial=None):
        """Reduce to single value"""
        if initial is None:
            result = self.data[0]
            start = 1
        else:
            result = initial
            start = 0

        for item in self.data[start:]:
            result = reducer(result, item)
        return result

    def get(self):
        """Get the data"""
        return self.data


print("=" * 60)
print("Example 7: Chainable Operations")
print("=" * 60)

numbers = ChainableList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Chain operations
result = (numbers
          .filter(lambda x: x % 2 == 0)  # Keep even numbers
          .map(lambda x: x ** 2)          # Square them
          .get())

print(f"Even numbers squared: {result}")

# Another chain
sum_result = (ChainableList([1, 2, 3, 4, 5])
              .map(lambda x: x * 2)
              .reduce(lambda a, b: a + b, 0))

print(f"Sum of doubled numbers: {sum_result}")
print()


# Example 8: Callable factory pattern
class ValidatorFactory:
    """Create validators on the fly"""

    @staticmethod
    def create_range_validator(min_val, max_val):
        """Create a range validator"""
        class RangeValidator:
            def __call__(self, value):
                return min_val <= value <= max_val

            def __repr__(self):
                return f"RangeValidator({min_val}, {max_val})"

        return RangeValidator()

    @staticmethod
    def create_length_validator(min_len, max_len):
        """Create a length validator"""
        class LengthValidator:
            def __call__(self, value):
                return min_len <= len(value) <= max_len

            def __repr__(self):
                return f"LengthValidator({min_len}, {max_len})"

        return LengthValidator()

    @staticmethod
    def create_pattern_validator(pattern):
        """Create a pattern validator"""
        import re

        class PatternValidator:
            def __call__(self, value):
                return bool(re.match(pattern, value))

            def __repr__(self):
                return f"PatternValidator('{pattern}')"

        return PatternValidator()


print("=" * 60)
print("Example 8: Validator Factory")
print("=" * 60)

# Create validators
age_validator = ValidatorFactory.create_range_validator(18, 100)
password_validator = ValidatorFactory.create_length_validator(8, 20)
email_validator = ValidatorFactory.create_pattern_validator(
    r'^[\w\.-]+@[\w\.-]+\.\w+$')

print(f"Age 25 valid? {age_validator(25)}")
print(f"Age 15 valid? {age_validator(15)}")
print()

print(f"Password 'short' valid? {password_validator('short')}")
print(f"Password 'longenough123' valid? {password_validator('longenough123')}")
print()

print(f"Email 'test@example.com' valid? {email_validator('test@example.com')}")
print(f"Email 'invalid' valid? {email_validator('invalid')}")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. Partial application creates specialized functions")
print("2. Lazy evaluation defers computation")
print("3. Function composition combines operations")
print("4. Pipelines chain transformations")
print("5. Retry mechanisms add resilience")
print("6. Chainable APIs improve readability")
print("7. Factories create callables dynamically")
