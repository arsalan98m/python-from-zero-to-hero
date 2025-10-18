"""
Default Values in Dataclasses
=============================

Learn how to set default values for dataclass fields
"""

from dataclasses import dataclass
from typing import Optional

# Example 1: Simple defaults


@dataclass
class Employee:
    name: str
    department: str
    salary: float
    is_manager: bool = False  # Default value
    years_experience: int = 0  # Default value


print("=" * 60)
print("Example 1: Employee with Defaults")
print("=" * 60)

# Creating employees with and without default values
emp1 = Employee("Alice Johnson", "Engineering", 95000)
emp2 = Employee("Bob Smith", "Engineering", 120000,
                is_manager=True, years_experience=8)

print(emp1)
print(emp2)
print()


# Example 2: User Account with Optional Fields
@dataclass
class UserAccount:
    username: str
    email: str
    is_active: bool = True
    is_verified: bool = False
    phone: Optional[str] = None  # Optional means can be None


print("=" * 60)
print("Example 2: User Accounts")
print("=" * 60)

user1 = UserAccount("john_doe", "john@example.com")
user2 = UserAccount("jane_smith", "jane@example.com", phone="+1-555-0123")
user3 = UserAccount("admin", "admin@example.com",
                    is_active=True, is_verified=True)

print(user1)
print(user2)
print(user3)
print()


# Example 3: Restaurant Order System
@dataclass
class Order:
    order_id: int
    customer_name: str
    items: str
    quantity: int = 1
    is_paid: bool = False
    tip: float = 0.0
    special_instructions: str = ""


print("=" * 60)
print("Example 3: Restaurant Orders")
print("=" * 60)

order1 = Order(1001, "Alice", "Pizza")
order2 = Order(1002, "Bob", "Burger", quantity=2, tip=5.0)
order3 = Order(1003, "Charlie", "Salad",
               special_instructions="No onions please")

print(order1)
print(order2)
print(order3)
print()


# Example 4: Social Media Post
@dataclass
class Post:
    post_id: int
    author: str
    content: str
    likes: int = 0
    comments: int = 0
    is_published: bool = True
    is_pinned: bool = False


print("=" * 60)
print("Example 4: Social Media Posts")
print("=" * 60)

post1 = Post(501, "tech_guru", "Just learned about Python dataclasses! 🚀")
post2 = Post(502, "food_lover", "Best pizza in town!", likes=150, comments=23)
post3 = Post(503, "admin", "Welcome to our community!", is_pinned=True)

print(post1)
print(post2)
print(post3)
print()

# Simulating user interactions
post1.likes += 10
post1.comments += 2

print("After some interactions:")
print(f"Post by {post1.author}: {post1.likes} likes, {post1.comments} comments")
print()


# IMPORTANT NOTE: Order of fields matters!
# Fields without defaults must come BEFORE fields with defaults

# This works ✓
@dataclass
class CorrectOrder:
    required_field: str  # No default
    optional_field: int = 0  # Has default


# This would cause an error ✗
# @dataclass
# class WrongOrder:
#     optional_field: int = 0  # Has default
#     required_field: str  # No default - ERROR!


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. Default values make fields optional")
print("2. Fields without defaults must come first")
print("3. Use Optional[Type] for fields that can be None")
print("4. Defaults improve code flexibility and usability")
