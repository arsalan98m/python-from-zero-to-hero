"""
Methods in Dataclasses
======================

Dataclasses can have methods just like regular classes!
"""

from dataclasses import dataclass
from typing import List

# Example 1: Bank Account with methods


@dataclass
class BankAccount:
    account_number: str
    holder_name: str
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account"""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False

        if amount > self.balance:
            print("Insufficient funds!")
            return False

        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True

    def get_balance(self) -> float:
        """Get current balance"""
        return self.balance


print("=" * 60)
print("Example 1: Bank Account Operations")
print("=" * 60)

account = BankAccount("ACC-12345", "Alice Johnson", 1000.0)
print(account)
print()

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Should fail
print(f"Current balance: ${account.get_balance():.2f}")
print()


# Example 2: Shopping Cart
@dataclass
class ShoppingCart:
    customer_name: str
    items: List[tuple] = None  # List of (item_name, price) tuples

    def __post_init__(self):
        """Initialize items list if None"""
        if self.items is None:
            self.items = []

    def add_item(self, item_name: str, price: float) -> None:
        """Add an item to the cart"""
        self.items.append((item_name, price))
        print(f"Added {item_name} (${price:.2f}) to cart")

    def remove_item(self, item_name: str) -> None:
        """Remove an item from the cart"""
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                print(f"Removed {item_name} from cart")
                return
        print(f"{item_name} not found in cart")

    def get_total(self) -> float:
        """Calculate total price"""
        return sum(price for _, price in self.items)

    def checkout(self) -> None:
        """Display checkout summary"""
        print(f"\n{'='*40}")
        print(f"Checkout for {self.customer_name}")
        print(f"{'='*40}")
        for item_name, price in self.items:
            print(f"  {item_name}: ${price:.2f}")
        print(f"{'='*40}")
        print(f"Total: ${self.get_total():.2f}")
        print(f"{'='*40}\n")


print("=" * 60)
print("Example 2: Shopping Cart")
print("=" * 60)

cart = ShoppingCart("Bob Smith")
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 29.99)
cart.add_item("Keyboard", 79.99)
cart.remove_item("Mouse")
cart.checkout()


# Example 3: Temperature Converter
@dataclass
class Temperature:
    celsius: float

    def to_fahrenheit(self) -> float:
        """Convert Celsius to Fahrenheit"""
        return (self.celsius * 9/5) + 32

    def to_kelvin(self) -> float:
        """Convert Celsius to Kelvin"""
        return self.celsius + 273.15

    def is_freezing(self) -> bool:
        """Check if temperature is at or below freezing"""
        return self.celsius <= 0

    def is_boiling(self) -> bool:
        """Check if temperature is at or above boiling"""
        return self.celsius >= 100

    def description(self) -> str:
        """Get a description of the temperature"""
        if self.celsius < 0:
            return "Freezing cold! ❄️"
        elif self.celsius < 15:
            return "Cold 🧊"
        elif self.celsius < 25:
            return "Comfortable 😊"
        elif self.celsius < 35:
            return "Warm ☀️"
        else:
            return "Very hot! 🔥"


print("=" * 60)
print("Example 3: Temperature Converter")
print("=" * 60)

temp1 = Temperature(25.0)
print(f"{temp1.celsius}°C = {temp1.to_fahrenheit():.1f}°F = {temp1.to_kelvin():.1f}K")
print(f"Description: {temp1.description()}")
print()

temp2 = Temperature(-5.0)
print(f"{temp2.celsius}°C = {temp2.to_fahrenheit():.1f}°F = {temp2.to_kelvin():.1f}K")
print(f"Is freezing? {temp2.is_freezing()}")
print(f"Description: {temp2.description()}")
print()


# Example 4: Student with Grade Calculator
@dataclass
class Student:
    name: str
    student_id: str
    grades: List[float] = None

    def __post_init__(self):
        if self.grades is None:
            self.grades = []

    def add_grade(self, grade: float) -> None:
        """Add a grade (0-100)"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Added grade {grade} for {self.name}")
        else:
            print("Grade must be between 0 and 100!")

    def get_average(self) -> float:
        """Calculate average grade"""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self) -> str:
        """Get letter grade based on average"""
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def report_card(self) -> None:
        """Print student report card"""
        print(f"\n{'='*40}")
        print(f"Report Card: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"{'='*40}")
        print(f"Grades: {', '.join(str(g) for g in self.grades)}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")
        print(f"{'='*40}\n")


print("=" * 60)
print("Example 4: Student Grade Management")
print("=" * 60)

student = Student("Emma Wilson", "S12345")
student.add_grade(95)
student.add_grade(87)
student.add_grade(92)
student.add_grade(88)
student.report_card()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. Dataclasses can have regular methods")
print("2. Methods can modify instance attributes")
print("3. Use __post_init__ for initialization logic")
print("4. Combine data storage with behavior")
