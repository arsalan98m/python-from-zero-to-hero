"""
Bounded TypeVars
================

Constrain TypeVars to specific types or classes
Useful when you need generic code but with some restrictions
"""

from typing import TypeVar, List, Protocol
from numbers import Number

# Example 1: Bounded TypeVar - Numeric Types
print("=" * 60)
print("Example 1: Numeric Bounded TypeVar")
print("=" * 60)

# Only allow numeric types
NumericType = TypeVar('NumericType', int, float)


def add_numbers(a: NumericType, b: NumericType) -> NumericType:
    """Add two numbers - only works with int or float"""
    return a + b  # type: ignore


result1 = add_numbers(5, 10)  # ✓ int
result2 = add_numbers(5.5, 2.3)  # ✓ float
# result3 = add_numbers("5", "10")  # ✗ Type error: str not allowed

print(f"add_numbers(5, 10) = {result1}")
print(f"add_numbers(5.5, 2.3) = {result2}")
print("Only int or float allowed!")
print()


# Example 2: Multiple Allowed Types
print("=" * 60)
print("Example 2: Multiple Allowed Types")
print("=" * 60)

StringOrBytes = TypeVar('StringOrBytes', str, bytes)


def get_length(data: StringOrBytes) -> int:
    """Get length of string or bytes"""
    return len(data)


def uppercase(data: StringOrBytes) -> StringOrBytes:
    """Convert to uppercase"""
    if isinstance(data, str):
        return data.upper()  # type: ignore
    return data.upper()  # type: ignore


text_len = get_length("hello")
bytes_len = get_length(b"world")

print(f"Length of 'hello': {text_len}")
print(f"Length of b'world': {bytes_len}")
print()

upper_text = uppercase("hello")
upper_bytes = uppercase(b"world")

print(f"Uppercase 'hello': {upper_text}")
print(f"Uppercase b'world': {upper_bytes}")
print()


# Example 3: Bounded by Base Class
print("=" * 60)
print("Example 3: Bounded by Class Inheritance")
print("=" * 60)


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Some sound"


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"


# TypeVar bound to Animal class and its subclasses
AnimalType = TypeVar('AnimalType', bound=Animal)


def make_animal_speak(animal: AnimalType) -> str:
    """Make any animal speak"""
    return animal.speak()


def get_animal_name(animal: AnimalType) -> str:
    """Get animal name"""
    return animal.name


dog = Dog("Buddy")
cat = Cat("Whiskers")

print(make_animal_speak(dog))
print(make_animal_speak(cat))
print(f"Dog name: {get_animal_name(dog)}")
print(f"Cat name: {get_animal_name(cat)}")
print()


# Example 4: Comparable Protocol
print("=" * 60)
print("Example 4: Bounded by Protocol")
print("=" * 60)


class Comparable(Protocol):
    """Protocol for comparable types"""

    def __lt__(self, other) -> bool:
        ...

    def __le__(self, other) -> bool:
        ...


ComparableType = TypeVar('ComparableType', bound=Comparable)


def find_min(items: List[ComparableType]) -> ComparableType:
    """Find minimum item - works with any comparable type"""
    if not items:
        raise ValueError("Empty list")

    min_item = items[0]
    for item in items[1:]:
        if item < min_item:
            min_item = item
    return min_item


def find_max(items: List[ComparableType]) -> ComparableType:
    """Find maximum item"""
    if not items:
        raise ValueError("Empty list")

    max_item = items[0]
    for item in items[1:]:
        if item > max_item:
            max_item = item
    return max_item


numbers = [5, 2, 8, 1, 9, 3]
words = ["zebra", "apple", "mango", "banana"]

print(f"Min number: {find_min(numbers)}")
print(f"Max number: {find_max(numbers)}")
print(f"Min word: {find_min(words)}")
print(f"Max word: {find_max(words)}")
print()


# Example 5: Real-world - Generic Sorter
print("=" * 60)
print("Example 5: Generic Sorter with Comparable Bound")
print("=" * 60)


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __lt__(self, other: 'Person') -> bool:
        return self.age < other.age

    def __le__(self, other: 'Person') -> bool:
        return self.age <= other.age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"


PersonType = TypeVar('PersonType', bound=Person)


def sort_by_age(people: List[PersonType]) -> List[PersonType]:
    """Sort people by age"""
    return sorted(people)


people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35),
    Person("Diana", 28)
]

sorted_people = sort_by_age(people)
print("People sorted by age:")
for person in sorted_people:
    print(f"  {person}")
print()


# Example 6: Number Operations with Bound
print("=" * 60)
print("Example 6: Numeric Operations")
print("=" * 60)

# Bound to Number base class
NumType = TypeVar('NumType', bound=Number)


def average(numbers: List[NumType]) -> float:
    """Calculate average of numbers"""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)  # type: ignore


def multiply_all(numbers: List[NumType], factor: NumType) -> List[NumType]:
    """Multiply all numbers by factor"""
    return [n * factor for n in numbers]  # type: ignore


integers = [1, 2, 3, 4, 5]
floats = [1.5, 2.5, 3.5, 4.5]

print(f"Average of {integers}: {average(integers)}")
print(f"Average of {floats}: {average(floats)}")
print()

doubled_ints = multiply_all(integers, 2)
doubled_floats = multiply_all(floats, 2.0)

print(f"Doubled integers: {doubled_ints}")
print(f"Doubled floats: {doubled_floats}")
print()


# Example 7: Container Operations
print("=" * 60)
print("Example 7: Container with Comparable Items")
print("=" * 60)


class SortedContainer(List[ComparableType]):
    """Container that keeps items sorted"""

    def add(self, item: ComparableType) -> None:
        """Add item and maintain sorted order"""
        self.append(item)
        self.sort()

    def get_min(self) -> ComparableType:
        """Get minimum item"""
        if not self:
            raise ValueError("Empty container")
        return self[0]

    def get_max(self) -> ComparableType:
        """Get maximum item"""
        if not self:
            raise ValueError("Empty container")
        return self[-1]


# Integer sorted container
int_container: SortedContainer[int] = SortedContainer()
int_container.add(5)
int_container.add(2)
int_container.add(8)
int_container.add(1)

print(f"Sorted integers: {list(int_container)}")
print(f"Min: {int_container.get_min()}")
print(f"Max: {int_container.get_max()}")
print()


# Example 8: Shape Hierarchy with Bounds
print("=" * 60)
print("Example 8: Shape Hierarchy")
print("=" * 60)


class Shape:
    """Base shape class"""

    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius


ShapeType = TypeVar('ShapeType', bound=Shape)


def total_area(shapes: List[ShapeType]) -> float:
    """Calculate total area of shapes"""
    return sum(shape.area() for shape in shapes)


def find_largest(shapes: List[ShapeType]) -> ShapeType:
    """Find shape with largest area"""
    if not shapes:
        raise ValueError("Empty list")
    return max(shapes, key=lambda s: s.area())


shapes: List[Shape] = [
    Rectangle(5, 3),
    Rectangle(4, 4),
    Circle(3),
    Circle(2)
]

print(f"Total area: {total_area(shapes):.2f}")
largest = find_largest(shapes)
print(f"Largest shape area: {largest.area():.2f}")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. Bounded TypeVars constrain allowed types")
print("2. Use 'bound' parameter for class hierarchies")
print("3. List specific types for exact constraints")
print("4. Protocols define interface requirements")
print("5. Enables generic code with type safety")
print("6. Type checker enforces constraints")
