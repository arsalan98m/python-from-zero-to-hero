"""
The field() Function
===================

The field() function provides additional control over dataclass fields
"""

import dataclasses
from dataclasses import dataclass, field
from typing import List, Dict
import random

# Example 1: Default Factory (for mutable defaults)
# WRONG WAY - Never use mutable defaults directly!
# @dataclass
# class WrongTodoList:
#     tasks: List[str] = []  # BAD! All instances share the same list


# CORRECT WAY - Use field(default_factory=...)
@dataclass
class TodoList:
    owner: str
    # Each instance gets a new list
    tasks: List[str] = field(default_factory=list)


print("=" * 60)
print("Example 1: Todo List with default_factory")
print("=" * 60)

alice_todos = TodoList("Alice")
bob_todos = TodoList("Bob")

alice_todos.tasks.append("Buy groceries")
alice_todos.tasks.append("Call mom")

bob_todos.tasks.append("Finish report")

print(f"{alice_todos.owner}'s tasks: {alice_todos.tasks}")
print(f"{bob_todos.owner}'s tasks: {bob_todos.tasks}")
print("Note: Each person has their own separate task list! ✓")
print()


# Example 2: Excluding Fields from __repr__
@dataclass
class User:
    username: str
    email: str
    password: str = field(repr=False)  # Don't show password in repr
    role: str = "user"


print("=" * 60)
print("Example 2: Hiding Sensitive Data")
print("=" * 60)

user = User("john_doe", "john@example.com", "super_secret_123")
print(user)  # Password won't be shown
print("Notice: Password is hidden in the output! 🔒")
print()


# Example 3: Excluding Fields from Comparison
@dataclass
class Product:
    product_id: int
    name: str
    price: float
    stock: int = field(compare=False)  # Don't use stock in comparison
    # Don't use timestamp in comparison
    last_updated: str = field(compare=False)


print("=" * 60)
print("Example 3: Custom Comparison")
print("=" * 60)

product1 = Product(101, "Laptop", 999.99, stock=10, last_updated="2025-01-01")
product2 = Product(101, "Laptop", 999.99, stock=5, last_updated="2025-01-15")

print(product1)
print(product2)
# True! (stock doesn't matter)
print(f"Are they equal? {product1 == product2}")
print("Note: Products are equal even with different stock levels! ✓")
print()


# Example 4: Excluding Fields from __init__
@dataclass
class Order:
    order_id: int
    customer: str
    total: float
    timestamp: str = field(init=False)  # Not in __init__, set automatically

    def __post_init__(self):
        from datetime import datetime
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


print("=" * 60)
print("Example 4: Auto-generated Fields")
print("=" * 60)

order1 = Order(1001, "Alice", 150.50)
order2 = Order(1002, "Bob", 89.99)

print(order1)
print(order2)
print("Note: Timestamp is automatically generated! ⏰")
print()


# Example 5: Combining Multiple field() Options
@dataclass
class BlogPost:
    post_id: int
    title: str
    content: str
    author: str
    tags: List[str] = field(default_factory=list)
    views: int = field(default=0, repr=False, compare=False)
    internal_notes: str = field(default="", repr=False, compare=False)


print("=" * 60)
print("Example 5: Complex Field Configuration")
print("=" * 60)

post1 = BlogPost(
    post_id=1,
    title="Introduction to Python Dataclasses",
    content="Dataclasses are awesome...",
    author="TechWriter"
)
post1.tags.append("python")
post1.tags.append("tutorial")
post1.views = 1500

post2 = BlogPost(
    post_id=1,
    title="Introduction to Python Dataclasses",
    content="Dataclasses are awesome...",
    author="TechWriter"
)
post2.tags.append("python")
post2.tags.append("tutorial")
post2.views = 3000  # Different views

print(post1)
print(post2)
print(f"Are they equal? {post1 == post2}")  # True (views don't matter)
print()


# Example 6: Real-world Game Character
@dataclass
class GameCharacter:
    name: str
    character_class: str
    level: int = 1
    health: int = 100
    mana: int = 50
    inventory: List[str] = field(default_factory=list)
    equipped_items: Dict[str, str] = field(default_factory=dict)
    stats: Dict[str, int] = field(default_factory=lambda: {
        "strength": 10,
        "intelligence": 10,
        "agility": 10
    })

    def level_up(self):
        """Level up the character"""
        self.level += 1
        self.health += 20
        self.mana += 10
        print(f"{self.name} leveled up to level {self.level}!")

    def add_to_inventory(self, item: str):
        """Add item to inventory"""
        self.inventory.append(item)
        print(f"Added {item} to {self.name}'s inventory")


print("=" * 60)
print("Example 6: Game Character System")
print("=" * 60)

warrior = GameCharacter("Aragorn", "Warrior")
mage = GameCharacter("Gandalf", "Mage", level=10)

warrior.add_to_inventory("Iron Sword")
warrior.add_to_inventory("Health Potion")
warrior.equipped_items["weapon"] = "Iron Sword"

print(warrior)
print()

mage.add_to_inventory("Magic Staff")
mage.add_to_inventory("Spell Book")

print(mage)
print()

warrior.level_up()
print()


# Example 7: Metadata (for advanced use)
@dataclass
class ConfigSetting:
    name: str
    value: str
    secret: bool = field(default=False, metadata={
                         "description": "Is this a secret config?"})
    required: bool = field(default=True, metadata={
                           "description": "Is this config required?"})


print("=" * 60)
print("Example 7: Field Metadata")
print("=" * 60)

config1 = ConfigSetting("API_KEY", "abc123", secret=True)
config2 = ConfigSetting("APP_NAME", "MyApp")

print(config1)
print(config2)

# Accessing metadata
fields = dataclasses.fields(ConfigSetting)
for f in fields:
    if f.metadata:
        print(f"Field '{f.name}': {f.metadata}")
print()


print("=" * 60)
print("Field() Options Summary:")
print("=" * 60)
print("• default_factory: For mutable defaults (lists, dicts)")
print("• repr: Include/exclude from __repr__ (default: True)")
print("• compare: Include/exclude from comparison (default: True)")
print("• init: Include/exclude from __init__ (default: True)")
print("• metadata: Store additional information about field")
