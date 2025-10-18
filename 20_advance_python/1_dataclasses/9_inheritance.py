"""
Inheritance with Dataclasses
============================

Dataclasses support inheritance just like regular classes
Child classes inherit fields and methods from parent classes
"""

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

# Example 1: Basic Inheritance


@dataclass
class Vehicle:
    brand: str
    model: str
    year: int

    def display_info(self):
        """Display basic vehicle info"""
        print(f"{self.year} {self.brand} {self.model}")


@dataclass
class Car(Vehicle):
    num_doors: int
    fuel_type: str


@dataclass
class Motorcycle(Vehicle):
    engine_cc: int
    has_sidecar: bool = False


print("=" * 60)
print("Example 1: Vehicle Inheritance")
print("=" * 60)

car = Car("Toyota", "Camry", 2024, 4, "Hybrid")
bike = Motorcycle("Harley-Davidson", "Street 750", 2024, 750)

print(car)
car.display_info()
print()

print(bike)
bike.display_info()
print()


# Example 2: Employee Hierarchy
@dataclass
class Employee:
    employee_id: int
    name: str
    email: str
    salary: float

    def get_annual_salary(self) -> float:
        """Calculate annual salary"""
        return self.salary * 12

    def display(self):
        """Display employee info"""
        print(f"{self.name} ({self.employee_id}): ${self.salary:,.2f}/month")


@dataclass
class Manager(Employee):
    team_size: int
    department: str
    bonus: float = 0.0

    def get_annual_salary(self) -> float:
        """Calculate annual salary including bonus"""
        return (self.salary * 12) + self.bonus


@dataclass
class Developer(Employee):
    programming_languages: List[str] = field(default_factory=list)
    projects: List[str] = field(default_factory=list)


@dataclass
class Intern(Employee):
    university: str
    graduation_year: int
    mentor: str


print("=" * 60)
print("Example 2: Employee Hierarchy")
print("=" * 60)

manager = Manager(
    employee_id=1,
    name="Alice Johnson",
    email="alice@company.com",
    salary=10000,
    team_size=5,
    department="Engineering",
    bonus=15000
)

developer = Developer(
    employee_id=2,
    name="Bob Smith",
    email="bob@company.com",
    salary=7500,
    programming_languages=["Python", "JavaScript", "Go"],
    projects=["Web App", "API Service"]
)

intern = Intern(
    employee_id=3,
    name="Charlie Brown",
    email="charlie@company.com",
    salary=2000,
    university="MIT",
    graduation_year=2026,
    mentor="Bob Smith"
)

print("Manager:")
manager.display()
print(f"Annual compensation: ${manager.get_annual_salary():,.2f}")
print()

print("Developer:")
developer.display()
print(f"Languages: {', '.join(developer.programming_languages)}")
print()

print("Intern:")
intern.display()
print(f"University: {intern.university}")
print()


# Example 3: Shapes with Polymorphism


@dataclass
class Shape(ABC):
    name: str

    @abstractmethod
    def area(self) -> float:
        """Calculate area"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate perimeter"""
        pass


@dataclass
class Rectangle(Shape):
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


@dataclass
class Circle(Shape):
    radius: float

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


@dataclass
class Triangle(Shape):
    side_a: float
    side_b: float
    side_c: float

    def area(self) -> float:
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c


print("=" * 60)
print("Example 3: Shapes (Polymorphism)")
print("=" * 60)

shapes = [
    Rectangle("Rectangle", 5.0, 3.0),
    Circle("Circle", 4.0),
    Triangle("Triangle", 3.0, 4.0, 5.0)
]

for shape in shapes:
    print(f"{shape.name}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")
    print()


# Example 4: User Account Hierarchy
@dataclass
class User:
    user_id: int
    username: str
    email: str
    created_at: str

    def display_info(self):
        """Display user information"""
        print(f"User: {self.username} ({self.email})")


@dataclass
class PremiumUser(User):
    subscription_end: str
    features: List[str] = field(default_factory=lambda: [
        "Ad-free",
        "HD streaming",
        "Priority support"
    ])

    def is_active(self) -> bool:
        """Check if subscription is active"""
        # Simplified check
        return True  # Would compare with current date

    def display_info(self):
        """Display premium user information"""
        super().display_info()
        print(f"Subscription: Premium (expires {self.subscription_end})")
        print(f"Features: {', '.join(self.features)}")


@dataclass
class AdminUser(User):
    permissions: List[str] = field(default_factory=lambda: [
        "read", "write", "delete", "manage_users"
    ])
    department: str = "IT"

    def has_permission(self, permission: str) -> bool:
        """Check if admin has specific permission"""
        return permission in self.permissions

    def display_info(self):
        """Display admin information"""
        super().display_info()
        print(f"Role: Administrator ({self.department})")
        print(f"Permissions: {', '.join(self.permissions)}")


print("=" * 60)
print("Example 4: User Account Types")
print("=" * 60)

regular_user = User(1, "john_doe", "john@example.com", "2025-01-01")
premium_user = PremiumUser(
    2, "jane_smith", "jane@example.com", "2024-06-01", "2025-12-31")
admin_user = AdminUser(3, "admin", "admin@example.com", "2020-01-01")

print("Regular User:")
regular_user.display_info()
print()

print("Premium User:")
premium_user.display_info()
print()

print("Admin User:")
admin_user.display_info()
print(f"Can delete? {admin_user.has_permission('delete')}")
print()


# Example 5: Product Catalog
@dataclass
class Product:
    product_id: int
    name: str
    price: float
    stock: int

    def is_available(self) -> bool:
        """Check if product is in stock"""
        return self.stock > 0


@dataclass
class DigitalProduct(Product):
    download_link: str
    file_size_mb: float
    stock: int = field(default=999999, init=False)  # Always available

    def is_available(self) -> bool:
        """Digital products are always available"""
        return True


@dataclass
class PhysicalProduct(Product):
    weight_kg: float
    dimensions: str  # "LxWxH cm"
    shipping_cost: float


print("=" * 60)
print("Example 5: Product Types")
print("=" * 60)

ebook = DigitalProduct(
    product_id=101,
    name="Python Programming Guide",
    price=29.99,
    stock=0,  # Will be overridden
    download_link="https://example.com/download/python-guide",
    file_size_mb=15.5
)

laptop = PhysicalProduct(
    product_id=102,
    name="Laptop Pro",
    price=1299.99,
    stock=5,
    weight_kg=1.8,
    dimensions="35x25x2",
    shipping_cost=15.00
)

print(ebook)
print(f"Available: {ebook.is_available()}")
print(f"File size: {ebook.file_size_mb}MB")
print()

print(laptop)
print(f"Available: {laptop.is_available()}")
print(f"Weight: {laptop.weight_kg}kg")
print(f"Shipping: ${laptop.shipping_cost}")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. Dataclasses support inheritance")
print("2. Child classes inherit all fields and methods")
print("3. Can override methods in child classes")
print("4. Can add new fields in child classes")
print("5. Use super() to call parent methods")
print("6. Works with abstract base classes (ABC)")
print("7. Field order: parent fields first, then child fields")
