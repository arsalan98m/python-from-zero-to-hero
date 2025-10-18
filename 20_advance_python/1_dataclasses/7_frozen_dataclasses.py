"""
Frozen Dataclasses (Immutability)
=================================

frozen=True makes dataclass instances immutable (like tuples)
Once created, you cannot modify the fields
"""

from dataclasses import dataclass, FrozenInstanceError

# Example 1: Basic Frozen Dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float


print("=" * 60)
print("Example 1: Frozen Point")
print("=" * 60)

point = Point(3.0, 4.0)
print(point)
print(f"X: {point.x}, Y: {point.y}")

# Try to modify (this will fail!)
try:
    point.x = 10.0  # ✗ Error!
except FrozenInstanceError as e:
    print(f"✗ Cannot modify: {e}")
print()


# Example 2: Why Use Frozen? - Configuration Settings
@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    port: int
    database: str
    username: str
    password: str


print("=" * 60)
print("Example 2: Immutable Configuration")
print("=" * 60)

config = DatabaseConfig(
    host="localhost",
    port=5432,
    database="myapp_db",
    username="admin",
    password="secret123"
)

print(config)

# Configuration should not be changed after creation!
try:
    config.host = "hackerserver.com"  # ✗ Prevented!
except FrozenInstanceError:
    print("✓ Configuration is protected from modification!")
print()


# Example 3: Frozen Dataclasses are Hashable
@dataclass(frozen=True)
class User:
    user_id: int
    username: str
    email: str


print("=" * 60)
print("Example 3: Hashable Objects (can be used in sets/dicts)")
print("=" * 60)

user1 = User(1, "alice", "alice@example.com")
user2 = User(2, "bob", "bob@example.com")
user3 = User(1, "alice", "alice@example.com")  # Duplicate

# Can use in sets (only possible with frozen dataclasses!)
users_set = {user1, user2, user3}
print(f"Unique users in set: {len(users_set)}")  # 2 (user1 and user3 are same)

# Can use as dictionary keys
user_data = {
    user1: "Premium member",
    user2: "Free member"
}
print(f"User1 status: {user_data[user1]}")
print()


# Example 4: Real-world - Geographic Coordinates
@dataclass(frozen=True)
class Coordinates:
    latitude: float
    longitude: float
    name: str

    def distance_to(self, other: 'Coordinates') -> float:
        """Calculate approximate distance in km (simplified)"""
        import math
        lat_diff = abs(self.latitude - other.latitude)
        lon_diff = abs(self.longitude - other.longitude)
        # Rough approximation
        return math.sqrt(lat_diff**2 + lon_diff**2) * 111


print("=" * 60)
print("Example 4: Geographic Locations (Immutable)")
print("=" * 60)

paris = Coordinates(48.8566, 2.3522, "Paris")
london = Coordinates(51.5074, -0.1278, "London")

print(paris)
print(london)

# Coordinates shouldn't change - they're fixed points!
try:
    paris.latitude = 50.0  # ✗ Error!
except FrozenInstanceError:
    print("✓ Geographic coordinates are immutable!")

print(f"Distance: {paris.distance_to(london):.1f} km (approx)")
print()


# Example 5: Money/Currency (should be immutable)
@dataclass(frozen=True)
class Money:
    amount: float
    currency: str

    def __add__(self, other: 'Money') -> 'Money':
        """Add two money amounts"""
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies!")
        return Money(self.amount + other.amount, self.currency)

    def __mul__(self, multiplier: float) -> 'Money':
        """Multiply money amount"""
        return Money(self.amount * multiplier, self.currency)


print("=" * 60)
print("Example 5: Immutable Money Operations")
print("=" * 60)

price = Money(100.00, "USD")
tax = Money(8.00, "USD")

total = price + tax
print(f"Price: {price}")
print(f"Tax: {tax}")
print(f"Total: {total}")

# Each operation creates a NEW object (immutable!)
doubled = price * 2
print(f"Doubled: {doubled}")
print(f"Original price unchanged: {price}")
print()


# Example 6: API Response (should not be modified)
@dataclass(frozen=True)
class APIResponse:
    status_code: int
    data: str
    timestamp: str

    def is_success(self) -> bool:
        """Check if response was successful"""
        return 200 <= self.status_code < 300


print("=" * 60)
print("Example 6: Immutable API Response")
print("=" * 60)

response = APIResponse(200, "{'message': 'Success'}", "2025-01-01T10:30:00")
print(response)
print(f"Success: {response.is_success()}")

# API responses should not be modified after reception
try:
    response.status_code = 500  # ✗ Error!
except FrozenInstanceError:
    print("✓ API response data is protected!")
print()


# Example 7: Comparing Mutable vs Immutable
@dataclass
class MutablePerson:
    name: str
    age: int


@dataclass(frozen=True)
class ImmutablePerson:
    name: str
    age: int


print("=" * 60)
print("Example 7: Mutable vs Immutable")
print("=" * 60)

# Mutable
mutable = MutablePerson("Alice", 30)
print(f"Mutable before: {mutable}")
mutable.age = 31  # ✓ Allowed
print(f"Mutable after: {mutable}")
print()

# Immutable
immutable = ImmutablePerson("Bob", 25)
print(f"Immutable: {immutable}")
try:
    immutable.age = 26  # ✗ Not allowed
except FrozenInstanceError:
    print("✗ Cannot modify frozen dataclass!")
print()

# Hashable test
try:
    print(f"Hash of immutable: {hash(immutable)}")  # ✓ Works
    print(f"Hash of mutable: {hash(mutable)}")  # ✗ Fails
except TypeError as e:
    print(f"✗ Mutable dataclass is not hashable: {e}")
print()


print("=" * 60)
print("When to Use frozen=True:")
print("=" * 60)
print("✓ Configuration objects (shouldn't change)")
print("✓ Coordinates, dates, timestamps")
print("✓ API responses")
print("✓ When you need hashable objects (for sets/dict keys)")
print("✓ Value objects (like Money, Temperature)")
print("✓ To prevent accidental modifications")
print("✗ When you need to modify fields after creation")
print()

print("=" * 60)
print("Benefits of Frozen Dataclasses:")
print("=" * 60)
print("1. Thread-safe (immutable = safe for concurrent access)")
print("2. Hashable (can use in sets and as dict keys)")
print("3. Prevents bugs from accidental modification")
print("4. Clear intent: this data should not change")
