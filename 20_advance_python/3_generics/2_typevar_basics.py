"""
TypeVar Basics
==============

TypeVar is the foundation of generics in Python
It creates a type variable that can represent any type
"""

from typing import TypeVar, List, Dict, Tuple, Optional

# Example 1: Creating TypeVars
print("=" * 60)
print("Example 1: Creating TypeVars")
print("=" * 60)

# Basic TypeVar
T = TypeVar('T')  # Can be any type
U = TypeVar('U')  # Different type variable
V = TypeVar('V')  # Another different type variable

print("T = TypeVar('T') - can represent any type")
print("U = TypeVar('U') - independent from T")
print("V = TypeVar('V') - independent from T and U")
print()


# Example 2: TypeVar in Function Signatures
print("=" * 60)
print("Example 2: Using TypeVar in Functions")
print("=" * 60)


def identity(value: T) -> T:
    """Return the same value - type is preserved"""
    return value


# Type is preserved!
num = identity(42)  # Type: int
text = identity("hello")  # Type: str
flag = identity(True)  # Type: bool

print(f"identity(42) = {num}")
print(f"identity('hello') = {text}")
print(f"identity(True) = {flag}")
print("Each call preserves the input type!")
print()


# Example 3: Multiple Parameters with Same TypeVar
print("=" * 60)
print("Example 3: Same Type for Multiple Parameters")
print("=" * 60)


def are_equal(a: T, b: T) -> bool:
    """Check if two values of same type are equal"""
    return a == b


# Both parameters must be same type
result1 = are_equal(5, 10)  # ✓ Both int
result2 = are_equal("hello", "world")  # ✓ Both str
# result3 = are_equal(5, "5")  # ✗ Type error: int vs str

print(f"are_equal(5, 10) = {result1}")
print(f"are_equal('hello', 'world') = {result2}")
print("Both parameters must be the same type!")
print()


# Example 4: Multiple Different TypeVars
print("=" * 60)
print("Example 4: Multiple Independent TypeVars")
print("=" * 60)


def make_pair(first: T, second: U) -> Tuple[T, U]:
    """Create a pair of values (can be different types)"""
    return (first, second)


# Different types allowed!
pair1 = make_pair(42, "answer")  # Type: Tuple[int, str]
pair2 = make_pair("name", 100)  # Type: Tuple[str, int]
pair3 = make_pair(1.5, True)  # Type: Tuple[float, bool]

print(f"make_pair(42, 'answer') = {pair1}")
print(f"make_pair('name', 100) = {pair2}")
print(f"make_pair(1.5, True) = {pair3}")
print("T and U are independent - can be different types!")
print()


# Example 5: Real-world - Find in List
print("=" * 60)
print("Example 5: Finding Items in List")
print("=" * 60)


def find_item(items: List[T], target: T) -> Optional[int]:
    """Find index of item in list"""
    try:
        return items.index(target)
    except ValueError:
        return None


numbers = [10, 20, 30, 40, 50]
words = ["apple", "banana", "cherry"]

idx1 = find_item(numbers, 30)
idx2 = find_item(words, "banana")
idx3 = find_item(numbers, 99)

print(f"Index of 30 in numbers: {idx1}")
print(f"Index of 'banana' in words: {idx2}")
print(f"Index of 99 in numbers: {idx3}")
print()


# Example 6: Real-world - Pair Class
print("=" * 60)
print("Example 6: Generic Pair Container")
print("=" * 60)


class Pair:
    """Store a pair of values (same type)"""

    def __init__(self, first: T, second: T):
        self.first = first
        self.second = second

    def swap(self) -> Tuple[T, T]:
        """Return swapped pair"""
        return (self.second, self.first)

    def both_equal(self) -> bool:
        """Check if both values are equal"""
        return self.first == self.second


# Note: Without Generic class (we'll learn later), this is just for demo
pair1 = Pair(10, 20)
pair2 = Pair("hello", "hello")

print(f"pair1: ({pair1.first}, {pair1.second})")
print(f"pair1 swapped: {pair1.swap()}")
print(f"pair1 equal? {pair1.both_equal()}")
print()

print(f"pair2: ({pair2.first}, {pair2.second})")
print(f"pair2 equal? {pair2.both_equal()}")
print()


# Example 7: Real-world - Filter and Transform
print("=" * 60)
print("Example 7: Generic Filter and Transform")
print("=" * 60)


def filter_items(items: List[T], predicate) -> List[T]:
    """Filter items using a predicate function"""
    return [item for item in items if predicate(item)]


def transform_items(items: List[T], transformer) -> List[T]:
    """Transform each item using a function"""
    return [transformer(item) for item in items]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = filter_items(numbers, lambda x: x % 2 == 0)
print(f"Even numbers: {evens}")

# Transform by squaring
squares = transform_items(numbers, lambda x: x ** 2)
print(f"Squared: {squares}")

words = ["hello", "world", "python"]
uppercase = transform_items(words, lambda x: x.upper())
print(f"Uppercase: {uppercase}")
print()


# Example 8: Real-world - Cache/Memoization
print("=" * 60)
print("Example 8: Generic Cache")
print("=" * 60)


class Cache:
    """Simple generic cache"""

    def __init__(self):
        self.data: Dict[str, T] = {}

    def set(self, key: str, value: T) -> None:
        """Store value in cache"""
        self.data[key] = value

    def get(self, key: str) -> Optional[T]:
        """Get value from cache"""
        return self.data.get(key)


# Integer cache
int_cache = Cache()
int_cache.set("user_id", 12345)
int_cache.set("count", 42)

print(f"user_id: {int_cache.get('user_id')}")
print(f"count: {int_cache.get('count')}")
print()

# String cache
str_cache = Cache()
str_cache.set("username", "alice")
str_cache.set("email", "alice@example.com")

print(f"username: {str_cache.get('username')}")
print(f"email: {str_cache.get('email')}")
print()


# Example 9: TypeVar Naming Conventions
print("=" * 60)
print("Example 9: TypeVar Naming Conventions")
print("=" * 60)

# Common conventions
T = TypeVar('T')  # Generic type (most common)
K = TypeVar('K')  # Key type (for dicts)
V = TypeVar('V')  # Value type (for dicts)
E = TypeVar('E')  # Element type
R = TypeVar('R')  # Return type

# Descriptive names
UserType = TypeVar('UserType')
ItemType = TypeVar('ItemType')

print("Common TypeVar names:")
print("  T - Generic type")
print("  K, V - Key, Value (for dictionaries)")
print("  E - Element")
print("  R - Return type")
print("  Or descriptive names like UserType, ItemType")
print()


# Example 10: Return Type Depends on Input
print("=" * 60)
print("Example 10: Type Preservation Through Operations")
print("=" * 60)


def double_list(items: List[T]) -> List[T]:
    """Double each element in list"""
    return items + items


def get_middle_item(items: List[T]) -> Optional[T]:
    """Get middle item from list"""
    if not items:
        return None
    mid = len(items) // 2
    return items[mid]


nums = [1, 2, 3]
doubled_nums = double_list(nums)  # Type: List[int]
middle_num = get_middle_item(nums)  # Type: Optional[int]

print(f"Original: {nums}")
print(f"Doubled: {doubled_nums}")
print(f"Middle: {middle_num}")
print()

words = ["a", "b", "c", "d", "e"]
doubled_words = double_list(words)  # Type: List[str]
middle_word = get_middle_item(words)  # Type: Optional[str]

print(f"Original: {words}")
print(f"Doubled: {doubled_words}")
print(f"Middle: {middle_word}")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. TypeVar creates a type placeholder")
print("2. Same TypeVar = same type throughout function")
print("3. Different TypeVars = can be different types")
print("4. Type is inferred from actual arguments")
print("5. Provides type safety without sacrificing flexibility")
print("6. Use T for generic type, K/V for key/value")
