"""
__post_init__ Method
===================

The __post_init__ method runs after the __init__ method
Perfect for validation, computed fields, and additional initialization
"""

from dataclasses import dataclass, field
from typing import List
import math

# Example 1: Validation in __post_init__


@dataclass
class Person:
    name: str
    age: int
    email: str

    def __post_init__(self):
        """Validate data after initialization"""
        if self.age < 0:
            raise ValueError("Age cannot be negative!")
        if self.age > 150:
            raise ValueError("Age seems unrealistic!")
        if "@" not in self.email:
            raise ValueError("Invalid email address!")

        print(f"✓ {self.name} created successfully")


print("=" * 60)
print("Example 1: Data Validation")
print("=" * 60)

try:
    person1 = Person("Alice", 30, "alice@example.com")
    person2 = Person("Bob", -5, "bob@example.com")  # Will fail
except ValueError as e:
    print(f"✗ Error: {e}")

print()


# Example 2: Computed Fields
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)  # Not in __init__, computed automatically
    perimeter: float = field(init=False)

    def __post_init__(self):
        """Calculate area and perimeter"""
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)


print("=" * 60)
print("Example 2: Computed Fields")
print("=" * 60)

rect = Rectangle(5.0, 3.0)
print(rect)
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")
print()


# Example 3: Real-world - Circle Calculator
@dataclass
class Circle:
    radius: float
    area: float = field(init=False, repr=False)
    circumference: float = field(init=False, repr=False)
    diameter: float = field(init=False, repr=False)

    def __post_init__(self):
        """Calculate all circle properties"""
        if self.radius <= 0:
            raise ValueError("Radius must be positive!")

        self.diameter = 2 * self.radius
        self.area = math.pi * self.radius ** 2
        self.circumference = 2 * math.pi * self.radius

    def display_info(self):
        """Display all circle information"""
        print(f"Circle with radius {self.radius}:")
        print(f"  Diameter: {self.diameter:.2f}")
        print(f"  Area: {self.area:.2f}")
        print(f"  Circumference: {self.circumference:.2f}")


print("=" * 60)
print("Example 3: Circle Calculator")
print("=" * 60)

circle = Circle(5.0)
circle.display_info()
print()


# Example 4: E-commerce Product with Discounts
@dataclass
class Product:
    name: str
    base_price: float
    discount_percent: float = 0
    final_price: float = field(init=False)
    savings: float = field(init=False)

    def __post_init__(self):
        """Calculate final price and savings"""
        if self.base_price < 0:
            raise ValueError("Price cannot be negative!")
        if not 0 <= self.discount_percent <= 100:
            raise ValueError("Discount must be between 0 and 100!")

        self.savings = self.base_price * (self.discount_percent / 100)
        self.final_price = self.base_price - self.savings


print("=" * 60)
print("Example 4: Product Pricing System")
print("=" * 60)

product1 = Product("Laptop", 1000, 15)
print(product1)
print(f"You save: ${product1.savings:.2f}!")
print()

product2 = Product("Phone", 800, 0)
print(product2)
print()


# Example 5: User Account with Auto-generated Username
@dataclass
class UserAccount:
    first_name: str
    last_name: str
    email: str
    username: str = field(init=False)
    full_name: str = field(init=False)

    def __post_init__(self):
        """Generate username and full name"""
        # Generate username from email
        self.username = self.email.split('@')[0]

        # Create full name
        self.full_name = f"{self.first_name} {self.last_name}"

        # Validation
        if not self.first_name or not self.last_name:
            raise ValueError("First name and last name are required!")


print("=" * 60)
print("Example 5: Auto-generated User Data")
print("=" * 60)

user1 = UserAccount("Alice", "Johnson", "alice.j@example.com")
user2 = UserAccount("Bob", "Smith", "bsmith@company.com")

print(user1)
print(f"Full name: {user1.full_name}")
print()
print(user2)
print(f"Full name: {user2.full_name}")
print()


# Example 6: BMI Calculator
@dataclass
class BMI:
    weight_kg: float
    height_m: float
    bmi: float = field(init=False)
    category: str = field(init=False)

    def __post_init__(self):
        """Calculate BMI and determine category"""
        if self.weight_kg <= 0 or self.height_m <= 0:
            raise ValueError("Weight and height must be positive!")

        # Calculate BMI
        self.bmi = self.weight_kg / (self.height_m ** 2)

        # Determine category
        if self.bmi < 18.5:
            self.category = "Underweight"
        elif self.bmi < 25:
            self.category = "Normal weight"
        elif self.bmi < 30:
            self.category = "Overweight"
        else:
            self.category = "Obese"

    def display_report(self):
        """Display health report"""
        print(f"Weight: {self.weight_kg}kg, Height: {self.height_m}m")
        print(f"BMI: {self.bmi:.1f} - {self.category}")


print("=" * 60)
print("Example 6: BMI Health Calculator")
print("=" * 60)

person1 = BMI(70, 1.75)
person1.display_report()
print()

person2 = BMI(90, 1.80)
person2.display_report()
print()


# Example 7: Order with Tax and Total Calculation
@dataclass
class Order:
    order_id: int
    items: List[tuple]  # List of (item_name, price)
    tax_rate: float = 0.08  # 8% tax
    subtotal: float = field(init=False)
    tax: float = field(init=False)
    total: float = field(init=False)

    def __post_init__(self):
        """Calculate subtotal, tax, and total"""
        self.subtotal = sum(price for _, price in self.items)
        self.tax = self.subtotal * self.tax_rate
        self.total = self.subtotal + self.tax

    def display_receipt(self):
        """Print order receipt"""
        print(f"\n{'='*40}")
        print(f"Order #{self.order_id}")
        print(f"{'='*40}")
        for item_name, price in self.items:
            print(f"  {item_name}: ${price:.2f}")
        print(f"{'='*40}")
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"Tax ({self.tax_rate*100}%): ${self.tax:.2f}")
        print(f"Total: ${self.total:.2f}")
        print(f"{'='*40}\n")


print("=" * 60)
print("Example 7: Order System with Calculations")
print("=" * 60)

order = Order(
    order_id=1001,
    items=[
        ("Laptop", 999.99),
        ("Mouse", 29.99),
        ("Keyboard", 79.99)
    ]
)

order.display_receipt()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. __post_init__ runs after __init__")
print("2. Perfect for validation and computed fields")
print("3. Use field(init=False) for computed fields")
print("4. Raise ValueError for invalid data")
print("5. Can transform or normalize input data")
