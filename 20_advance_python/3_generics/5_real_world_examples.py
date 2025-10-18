"""
Real-World Examples of Generics
===============================

Practical applications of generics in real systems
"""

from typing import TypeVar, Generic, List, Optional, Dict, Callable, Protocol
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')


# Example 1: API Response Wrapper
print("=" * 60)
print("Example 1: Generic API Response")
print("=" * 60)


class Status(Enum):
    SUCCESS = "success"
    ERROR = "error"
    LOADING = "loading"


@dataclass
class APIResponse(Generic[T]):
    """Generic API response wrapper"""
    status: Status
    data: Optional[T] = None
    error: Optional[str] = None
    timestamp: datetime = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

    def is_success(self) -> bool:
        return self.status == Status.SUCCESS

    def get_data(self) -> Optional[T]:
        return self.data if self.is_success() else None


@dataclass
class User:
    id: int
    name: str
    email: str


@dataclass
class Product:
    id: int
    name: str
    price: float


# Simulate API calls
def fetch_user(user_id: int) -> APIResponse[User]:
    """Fetch user from API"""
    if user_id > 0:
        user = User(user_id, "Alice", "alice@example.com")
        return APIResponse(Status.SUCCESS, data=user)
    return APIResponse(Status.ERROR, error="User not found")


def fetch_products() -> APIResponse[List[Product]]:
    """Fetch products from API"""
    products = [
        Product(1, "Laptop", 999.99),
        Product(2, "Mouse", 29.99),
        Product(3, "Keyboard", 79.99)
    ]
    return APIResponse(Status.SUCCESS, data=products)


# Use the API
user_response = fetch_user(1)
if user_response.is_success():
    user = user_response.get_data()
    print(f"User: {user.name} ({user.email})")

products_response = fetch_products()
if products_response.is_success():
    products = products_response.get_data()
    print(f"Found {len(products)} products")
    for product in products:
        print(f"  - {product.name}: ${product.price}")
print()


# Example 2: Generic Repository Pattern
print("=" * 60)
print("Example 2: Generic Repository Pattern")
print("=" * 60)


class Identifiable(Protocol):
    """Protocol for objects with an ID"""
    id: int


ModelType = TypeVar('ModelType', bound=Identifiable)


class Repository(Generic[ModelType]):
    """Generic repository for CRUD operations"""

    def __init__(self):
        self._storage: Dict[int, ModelType] = {}
        self._next_id = 1

    def create(self, item: ModelType) -> ModelType:
        """Create new item"""
        if not hasattr(item, 'id') or item.id is None:
            item.id = self._next_id
            self._next_id += 1
        self._storage[item.id] = item
        return item

    def get_by_id(self, item_id: int) -> Optional[ModelType]:
        """Get item by ID"""
        return self._storage.get(item_id)

    def get_all(self) -> List[ModelType]:
        """Get all items"""
        return list(self._storage.values())

    def update(self, item: ModelType) -> bool:
        """Update existing item"""
        if item.id in self._storage:
            self._storage[item.id] = item
            return True
        return False

    def delete(self, item_id: int) -> bool:
        """Delete item by ID"""
        if item_id in self._storage:
            del self._storage[item_id]
            return True
        return False

    def count(self) -> int:
        """Count all items"""
        return len(self._storage)

    def find(self, predicate: Callable[[ModelType], bool]) -> List[ModelType]:
        """Find items matching predicate"""
        return [item for item in self._storage.values() if predicate(item)]


@dataclass
class Task:
    id: Optional[int]
    title: str
    completed: bool = False
    priority: int = 1


# Task repository
task_repo: Repository[Task] = Repository()

# Create tasks
task1 = task_repo.create(Task(None, "Write documentation", priority=2))
task2 = task_repo.create(Task(None, "Fix bug", priority=3))
task3 = task_repo.create(Task(None, "Review code", completed=True, priority=1))

print("All tasks:")
for task in task_repo.get_all():
    status = "✓" if task.completed else "○"
    print(f"  {status} [{task.priority}] {task.title}")

# Find high priority tasks
high_priority = task_repo.find(lambda t: t.priority >= 2 and not t.completed)
print(f"\nHigh priority incomplete tasks: {len(high_priority)}")
for task in high_priority:
    print(f"  - {task.title}")
print()


# Example 3: Observable Pattern
print("=" * 60)
print("Example 3: Generic Observable Pattern")
print("=" * 60)


class Observable(Generic[T]):
    """Observable value that notifies listeners on change"""

    def __init__(self, initial_value: T):
        self._value = initial_value
        self._listeners: List[Callable[[T], None]] = []

    def get(self) -> T:
        """Get current value"""
        return self._value

    def set(self, new_value: T) -> None:
        """Set new value and notify listeners"""
        old_value = self._value
        self._value = new_value
        if old_value != new_value:
            self._notify()

    def subscribe(self, listener: Callable[[T], None]) -> None:
        """Subscribe to value changes"""
        self._listeners.append(listener)

    def _notify(self) -> None:
        """Notify all listeners"""
        for listener in self._listeners:
            listener(self._value)


# Temperature monitor
temperature: Observable[float] = Observable(20.0)


def on_temp_change(temp: float):
    if temp > 30:
        print(f"  ⚠️ HIGH TEMPERATURE: {temp}°C")
    elif temp < 10:
        print(f"  ⚠️ LOW TEMPERATURE: {temp}°C")
    else:
        print(f"  ✓ Normal temperature: {temp}°C")


temperature.subscribe(on_temp_change)

print("Temperature changes:")
temperature.set(25.0)
temperature.set(35.0)
temperature.set(5.0)
print()


# Example 4: Generic Builder Pattern
print("=" * 60)
print("Example 4: Generic Builder Pattern")
print("=" * 60)


class Builder(Generic[T]):
    """Generic builder pattern"""

    def __init__(self, factory: Callable[[], T]):
        self._factory = factory
        self._actions: List[Callable[[T], None]] = []

    def with_action(self, action: Callable[[T], None]) -> 'Builder[T]':
        """Add configuration action"""
        self._actions.append(action)
        return self

    def build(self) -> T:
        """Build the object"""
        obj = self._factory()
        for action in self._actions:
            action(obj)
        return obj


@dataclass
class Email:
    to: str = ""
    subject: str = ""
    body: str = ""
    attachments: List[str] = None

    def __post_init__(self):
        if self.attachments is None:
            self.attachments = []


# Build email
email = (Builder(Email)
         .with_action(lambda e: setattr(e, 'to', 'alice@example.com'))
         .with_action(lambda e: setattr(e, 'subject', 'Hello'))
         .with_action(lambda e: setattr(e, 'body', 'This is a test email'))
         .with_action(lambda e: e.attachments.append('document.pdf'))
         .build())

print("Built email:")
print(f"  To: {email.to}")
print(f"  Subject: {email.subject}")
print(f"  Body: {email.body}")
print(f"  Attachments: {email.attachments}")
print()


# Example 5: Generic State Machine
print("=" * 60)
print("Example 5: Generic State Machine")
print("=" * 60)


class StateMachine(Generic[T]):
    """Generic state machine"""

    def __init__(self, initial_state: T):
        self._current_state = initial_state
        self._transitions: Dict[tuple, T] = {}
        self._on_transition: Optional[Callable[[T, T], None]] = None

    def add_transition(self, from_state: T, event: str, to_state: T) -> None:
        """Add state transition"""
        self._transitions[(from_state, event)] = to_state

    def trigger(self, event: str) -> bool:
        """Trigger event to change state"""
        key = (self._current_state, event)
        if key in self._transitions:
            old_state = self._current_state
            self._current_state = self._transitions[key]
            if self._on_transition:
                self._on_transition(old_state, self._current_state)
            return True
        return False

    def get_state(self) -> T:
        """Get current state"""
        return self._current_state

    def on_transition(self, callback: Callable[[T, T], None]) -> None:
        """Set transition callback"""
        self._on_transition = callback


class OrderState(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


# Order state machine
order_sm: StateMachine[OrderState] = StateMachine(OrderState.PENDING)

# Define transitions
order_sm.add_transition(OrderState.PENDING, "process", OrderState.PROCESSING)
order_sm.add_transition(OrderState.PROCESSING, "ship", OrderState.SHIPPED)
order_sm.add_transition(OrderState.SHIPPED, "deliver", OrderState.DELIVERED)
order_sm.add_transition(OrderState.PENDING, "cancel", OrderState.CANCELLED)
order_sm.add_transition(OrderState.PROCESSING, "cancel", OrderState.CANCELLED)

# Set transition callback


def on_state_change(old: OrderState, new: OrderState):
    print(f"  Order state: {old.value} → {new.value}")


order_sm.on_transition(on_state_change)

# Simulate order flow
print("Order lifecycle:")
print(f"Initial state: {order_sm.get_state().value}")
order_sm.trigger("process")
order_sm.trigger("ship")
order_sm.trigger("deliver")
print(f"Final state: {order_sm.get_state().value}")
print()


# Example 6: Generic Validator Chain
print("=" * 60)
print("Example 6: Generic Validator Chain")
print("=" * 60)


class Validator(Generic[T]):
    """Generic validator"""

    def __init__(self, name: str, check: Callable[[T], bool], error_message: str):
        self.name = name
        self.check = check
        self.error_message = error_message

    def validate(self, value: T) -> Optional[str]:
        """Validate value, return error message if invalid"""
        return None if self.check(value) else self.error_message


class ValidationResult(Generic[T]):
    """Result of validation"""

    def __init__(self, value: T, errors: List[str] = None):
        self.value = value
        self.errors = errors or []

    def is_valid(self) -> bool:
        return len(self.errors) == 0


class ValidatorChain(Generic[T]):
    """Chain of validators"""

    def __init__(self):
        self.validators: List[Validator[T]] = []

    def add(self, validator: Validator[T]) -> 'ValidatorChain[T]':
        """Add validator to chain"""
        self.validators.append(validator)
        return self

    def validate(self, value: T) -> ValidationResult[T]:
        """Validate value through all validators"""
        errors = []
        for validator in self.validators:
            error = validator.validate(value)
            if error:
                errors.append(error)
        return ValidationResult(value, errors)


# Email validation chain
email_validator = ValidatorChain[str]()
email_validator.add(
    Validator("not_empty", lambda s: len(s) > 0, "Email cannot be empty")
).add(
    Validator("has_at", lambda s: "@" in s, "Email must contain @")
).add(
    Validator("has_domain", lambda s: "." in s.split(
        "@")[-1], "Email must have domain")
).add(
    Validator("min_length", lambda s: len(s) >= 5, "Email too short")
)

# Test emails
test_emails = ["alice@example.com", "invalid", "@", "a@b"]

print("Email validation:")
for email in test_emails:
    result = email_validator.validate(email)
    if result.is_valid():
        print(f"  ✓ {email}")
    else:
        print(f"  ✗ {email}")
        for error in result.errors:
            print(f"    - {error}")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. Generics make APIs type-safe and reusable")
print("2. Repository pattern benefits from generics")
print("3. Observable pattern with type safety")
print("4. State machines with typed states")
print("5. Validation chains preserve types")
print("6. Builder pattern with generic objects")
