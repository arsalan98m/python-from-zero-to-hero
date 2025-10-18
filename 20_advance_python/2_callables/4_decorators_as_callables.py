"""
Decorators Using Callables
==========================

Decorators can be implemented using callable classes
This gives more flexibility than function-based decorators
"""

import time
import functools

# Example 1: Basic decorator class


class SimpleDecorator:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"Finished {self.func.__name__}")
        return result


print("=" * 60)
print("Example 1: Basic Decorator Class")
print("=" * 60)


@SimpleDecorator
def say_hello(name):
    print(f"Hello, {name}!")
    return f"Greeted {name}"


result = say_hello("Alice")
print(f"Returned: {result}")
print()


# Example 2: Timer decorator
class Timer:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"{self.func.__name__} took {end - start:.4f} seconds")
        return result


print("=" * 60)
print("Example 2: Timer Decorator")
print("=" * 60)


@Timer
def slow_function():
    """Simulate slow operation"""
    time.sleep(0.5)
    return "Done!"


result = slow_function()
print(f"Result: {result}")
print()


# Example 3: Counter decorator with state
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

    def reset(self):
        """Reset the counter"""
        self.count = 0


print("=" * 60)
print("Example 3: Call Counter")
print("=" * 60)


@CountCalls
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))
print(f"Total calls: {greet.count}")

greet.reset()
print(f"After reset: {greet.count}")
print()


# Example 4: Decorator with parameters
class Repeat:
    def __init__(self, times):
        """Decorator that takes parameters"""
        self.times = times

    def __call__(self, func):
        """This is called during decoration"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """This is called when decorated function is called"""
            results = []
            for i in range(self.times):
                print(f"Execution {i+1}/{self.times}")
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper


print("=" * 60)
print("Example 4: Decorator with Parameters")
print("=" * 60)


@Repeat(times=3)
def say_hi():
    return "Hi!"


results = say_hi()
print(f"Results: {results}")
print()


# Example 5: Validation decorator
class ValidateTypes:
    def __init__(self, *expected_types):
        self.expected_types = expected_types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Check positional arguments
            for arg, expected_type in zip(args, self.expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Expected {expected_type.__name__}, "
                        f"got {type(arg).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper


print("=" * 60)
print("Example 5: Type Validation Decorator")
print("=" * 60)


@ValidateTypes(str, int)
def create_user(name, age):
    return f"User: {name}, Age: {age}"


# Valid call
result1 = create_user("Alice", 30)
print(result1)

# Invalid call
try:
    result2 = create_user("Bob", "thirty")  # Wrong type!
except TypeError as e:
    print(f"Error: {e}")
print()


# Example 6: Cache/Memoization decorator
class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)

    def __call__(self, *args):
        if args in self.cache:
            print(f"Cache hit for {args}")
            return self.cache[args]

        print(f"Computing for {args}")
        result = self.func(*args)
        self.cache[args] = result
        return result

    def clear_cache(self):
        """Clear the cache"""
        self.cache.clear()


print("=" * 60)
print("Example 6: Memoization Decorator")
print("=" * 60)


@Memoize
def fibonacci(n):
    """Calculate fibonacci number (inefficiently without cache)"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(f"fib(5) = {fibonacci(5)}")
print(f"fib(5) again = {fibonacci(5)}")  # Will use cache
print(f"fib(10) = {fibonacci(10)}")
print()


# Example 7: Rate limiter
class RateLimit:
    def __init__(self, max_calls, time_window):
        """
        Limit function calls
        max_calls: maximum number of calls
        time_window: time window in seconds
        """
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = []

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()

            # Remove old calls outside time window
            self.calls = [call_time for call_time in self.calls
                          if now - call_time < self.time_window]

            if len(self.calls) >= self.max_calls:
                raise Exception(
                    f"Rate limit exceeded: {self.max_calls} calls "
                    f"per {self.time_window} seconds"
                )

            self.calls.append(now)
            return func(*args, **kwargs)

        return wrapper


print("=" * 60)
print("Example 7: Rate Limiting")
print("=" * 60)


@RateLimit(max_calls=3, time_window=2)
def api_call(endpoint):
    return f"Called {endpoint}"


try:
    print(api_call("/users"))
    print(api_call("/posts"))
    print(api_call("/comments"))
    print(api_call("/likes"))  # This should fail
except Exception as e:
    print(f"Error: {e}")
print()


# Example 8: Debug decorator
class Debug:
    def __init__(self, prefix="DEBUG"):
        self.prefix = prefix

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)

            print(f"{self.prefix}: Calling {func.__name__}({signature})")
            result = func(*args, **kwargs)
            print(f"{self.prefix}: {func.__name__} returned {result!r}")

            return result
        return wrapper


print("=" * 60)
print("Example 8: Debug Decorator")
print("=" * 60)


@Debug(prefix="[LOG]")
def add(a, b):
    return a + b


@Debug(prefix="[TRACE]")
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


result1 = add(5, 3)
result2 = greet("Alice", greeting="Hi")
print()


# Example 9: Access control decorator
class RequireAuth:
    def __init__(self, required_role):
        self.required_role = required_role

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if not hasattr(user, 'role'):
                raise PermissionError("User has no role")

            if user.role != self.required_role:
                raise PermissionError(
                    f"Requires {self.required_role} role, "
                    f"user has {user.role}"
                )

            return func(user, *args, **kwargs)
        return wrapper


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


print("=" * 60)
print("Example 9: Access Control")
print("=" * 60)


@RequireAuth("admin")
def delete_user(user, target_id):
    return f"{user.name} deleted user {target_id}"


admin = User("Alice", "admin")
regular_user = User("Bob", "user")

# Admin can delete
try:
    result = delete_user(admin, 123)
    print(result)
except PermissionError as e:
    print(f"Error: {e}")

# Regular user cannot delete
try:
    result = delete_user(regular_user, 123)
    print(result)
except PermissionError as e:
    print(f"Error: {e}")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. Decorators can be implemented as callable classes")
print("2. Class decorators can maintain state (counters, caches)")
print("3. Use __init__ to set up decorator")
print("4. Use __call__ to wrap the function")
print("5. More flexible than function decorators")
print("6. Can add methods (reset, clear_cache, etc.)")
