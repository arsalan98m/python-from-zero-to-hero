"""
Introduction to Generics in Python
==================================

What are Generics?
- Generics allow you to write code that works with multiple types
- Provide type safety without sacrificing flexibility
- Help IDEs and type checkers catch errors early
- Make code more reusable and maintainable

Why use Generics?
- Write functions/classes that work with any type
- Maintain type information through operations
- Get better IDE autocomplete and error detection
- Document expected types clearly
"""

from typing import TypeVar
from typing import List, Dict, Tuple, Optional

# Example 1: The Problem - Without Generics
print("=" * 60)
print("Example 1: The Problem Without Type Hints")
print("=" * 60)


def get_first_item(items):
    """Get first item from list - what type does it return?"""
    if items:
        return items[0]
    return None


# What type is result? We don't know!
result1 = get_first_item([1, 2, 3])
result2 = get_first_item(["a", "b", "c"])

print(f"result1 = {result1}, type: {type(result1)}")
print(f"result2 = {result2}, type: {type(result2)}")
print("Problem: Type checker doesn't know the return type!")
print()


# Example 2: Basic Type Hints (Not Generic Yet)
print("=" * 60)
print("Example 2: Basic Type Hints")
print("=" * 60)


def get_first_int(items: List[int]) -> Optional[int]:
    """Get first integer from list"""
    if items:
        return items[0]
    return None


def get_first_str(items: List[str]) -> Optional[str]:
    """Get first string from list"""
    if items:
        return items[0]
    return None


int_result = get_first_int([1, 2, 3])
str_result = get_first_str(["a", "b", "c"])

print(f"int_result = {int_result}")
print(f"str_result = {str_result}")
print("Problem: We need different functions for each type!")
print()


# Example 3: Introduction to TypeVar (Generic Solution)

T = TypeVar('T')  # T can be any type


def get_first_item_generic(items: List[T]) -> Optional[T]:
    """Get first item - works with any type!"""
    if items:
        return items[0]
    return None


print("=" * 60)
print("Example 3: Generic Function with TypeVar")
print("=" * 60)

# Type checker knows the return type!
int_result = get_first_item_generic([1, 2, 3])  # Type: Optional[int]
str_result = get_first_item_generic(["a", "b", "c"])  # Type: Optional[str]
float_result = get_first_item_generic([1.5, 2.5])  # Type: Optional[float]

print(f"int_result = {int_result}")
print(f"str_result = {str_result}")
print(f"float_result = {float_result}")
print("Solution: One function works for all types with type safety!")
print()


# Example 4: Real-world - Stack with Generics
print("=" * 60)
print("Example 4: Generic Stack Container")
print("=" * 60)


class Stack:
    """Stack without generics - loses type information"""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None


# Using Stack - type checker doesn't know types
int_stack = Stack()
int_stack.push(1)
int_stack.push(2)
value = int_stack.pop()  # Type: Unknown!

print(f"Popped value: {value}")
print("Problem: Type checker doesn't know what type pop() returns")
print()


# Example 5: Comparing with and without generics
print("=" * 60)
print("Example 5: Type Safety Comparison")
print("=" * 60)

# Without generics


def swap_without_types(a, b):
    """Swap two values"""
    return b, a


x1, y1 = swap_without_types(5, 10)
print(f"Swapped: {x1}, {y1}")
print("Type checker knows nothing about x1 and y1")
print()

# With type hints (but specific)


def swap_ints(a: int, b: int) -> Tuple[int, int]:
    """Swap two integers"""
    return b, a


x2, y2 = swap_ints(5, 10)
print(f"Swapped: {x2}, {y2}")
print("Type checker knows they're ints, but only works for ints")
print()

# With generics (best solution)


def swap_generic(a: T, b: T) -> Tuple[T, T]:
    """Swap two values of same type"""
    return b, a


x3, y3 = swap_generic(5, 10)  # Type: Tuple[int, int]
x4, y4 = swap_generic("hello", "world")  # Type: Tuple[str, str]

print(f"Swapped ints: {x3}, {y3}")
print(f"Swapped strings: {x4}, {y4}")
print("Type checker knows exact types, works for any type!")
print()


# Example 6: Generic with List operations
print("=" * 60)
print("Example 6: Generic List Operations")
print("=" * 60)


def get_last_item(items: List[T]) -> Optional[T]:
    """Get last item from list"""
    return items[-1] if items else None


def reverse_list(items: List[T]) -> List[T]:
    """Reverse a list"""
    return items[::-1]


numbers = [1, 2, 3, 4, 5]
words = ["apple", "banana", "cherry"]

last_num = get_last_item(numbers)  # Type: Optional[int]
last_word = get_last_item(words)  # Type: Optional[str]

reversed_nums = reverse_list(numbers)  # Type: List[int]
reversed_words = reverse_list(words)  # Type: List[str]

print(f"Last number: {last_num}")
print(f"Last word: {last_word}")
print(f"Reversed numbers: {reversed_nums}")
print(f"Reversed words: {reversed_words}")
print()


# Example 7: Why Generics Matter - Type Safety
print("=" * 60)
print("Example 7: Type Safety in Action")
print("=" * 60)


def process_items(items: List[T]) -> T:
    """Process items and return first one"""
    if not items:
        raise ValueError("Empty list")
    return items[0]


# Type checker can catch errors!
result_int = process_items([1, 2, 3])  # ✓ Type: int
result_str = process_items(["a", "b"])  # ✓ Type: str

print(f"Processed int: {result_int}")
print(f"Processed str: {result_str}")

# If you try to use wrong type, type checker warns you:
# result_int.upper()  # ✗ Error: int has no method 'upper'
# result_str + 5      # ✗ Error: can't add str and int

print("\nType checker prevents runtime errors!")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. Generics allow writing type-safe, reusable code")
print("2. TypeVar creates a type variable (placeholder)")
print("3. Generic functions work with any type while preserving type info")
print("4. IDEs and type checkers use generics for better error detection")
print("5. One generic function can replace many type-specific functions")
print()

print("=" * 60)
print("Benefits of Generics:")
print("=" * 60)
print("✓ Code reusability")
print("✓ Type safety")
print("✓ Better IDE support")
print("✓ Self-documenting code")
print("✓ Catch errors before runtime")
