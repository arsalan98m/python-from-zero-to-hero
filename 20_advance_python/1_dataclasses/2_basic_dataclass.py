"""
Basic Dataclass Creation
========================

Step-by-step guide to creating and using dataclasses
"""

from dataclasses import dataclass

# Example 1: Simple Book dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float


print("=" * 60)
print("Example 1: Book Store")
print("=" * 60)

# Creating instances
book1 = Book("1984", "George Orwell", 328, 15.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 336, 14.99)
book3 = Book("1984", "George Orwell", 328, 15.99)

print(book1)
print(book2)
print()

# Automatic equality comparison
print(f"book1 == book2: {book1 == book2}")  # False
print(f"book1 == book3: {book1 == book3}")  # True
print()


# Example 2: Real-life Product in E-commerce
@dataclass
class Product:
    product_id: int
    name: str
    category: str
    price: float
    in_stock: bool


print("=" * 60)
print("Example 2: E-commerce Product")
print("=" * 60)

laptop = Product(
    product_id=101,
    name="MacBook Pro",
    category="Electronics",
    price=1999.99,
    in_stock=True
)

phone = Product(
    product_id=102,
    name="iPhone 15",
    category="Electronics",
    price=999.99,
    in_stock=False
)

print(laptop)
print(phone)
print()

# Accessing attributes
print(f"Product: {laptop.name}")
print(f"Price: ${laptop.price}")
print(f"Available: {laptop.in_stock}")
print()


# Example 3: Student Record System
@dataclass
class Student:
    student_id: str
    name: str
    grade: int
    gpa: float


print("=" * 60)
print("Example 3: Student Management System")
print("=" * 60)

student1 = Student("S001", "Emma Watson", 12, 3.95)
student2 = Student("S002", "Tom Holland", 11, 3.75)

print(student1)
print(student2)
print()

# Creating a list of students
students = [student1, student2]
print("All Students:")
for student in students:
    print(f"  {student.name} (Grade {student.grade}) - GPA: {student.gpa}")
print()


# Example 4: Coordinates (for mapping applications)
@dataclass
class Location:
    latitude: float
    longitude: float
    name: str


print("=" * 60)
print("Example 4: GPS Locations")
print("=" * 60)

eiffel_tower = Location(48.8584, 2.2945, "Eiffel Tower")
statue_of_liberty = Location(40.6892, -74.0445, "Statue of Liberty")

print(eiffel_tower)
print(statue_of_liberty)
print()

print(f"{eiffel_tower.name} coordinates: ({eiffel_tower.latitude}, {eiffel_tower.longitude})")
