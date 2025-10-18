"""
Practical Real-World Examples of Callables
==========================================

Real-world use cases where callables shine
"""

from typing import Callable, List, Any
import time


# Example 1: Event System with Callbacks
class EventEmitter:
    """Simple event emitter using callables as callbacks"""

    def __init__(self):
        self.listeners = {}

    def on(self, event_name: str, callback: Callable):
        """Register a callback for an event"""
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    def emit(self, event_name: str, *args, **kwargs):
        """Trigger all callbacks for an event"""
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                callback(*args, **kwargs)


print("=" * 60)
print("Example 1: Event System")
print("=" * 60)

emitter = EventEmitter()

# Register event handlers


def on_user_login(username):
    print(f"  [LOG] User logged in: {username}")


def send_welcome_email(username):
    print(f"  [EMAIL] Sending welcome email to {username}")


def update_last_login(username):
    print(f"  [DB] Updated last login time for {username}")


# Register multiple handlers for same event
emitter.on('user_login', on_user_login)
emitter.on('user_login', send_welcome_email)
emitter.on('user_login', update_last_login)

# Trigger the event
print("User 'Alice' logging in...")
emitter.emit('user_login', 'Alice')
print()


# Example 2: Strategy Pattern for Payment Processing
class PaymentStrategy:
    """Base class for payment strategies"""

    def __call__(self, amount: float) -> dict:
        raise NotImplementedError


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def __call__(self, amount: float) -> dict:
        # Simulate payment processing
        return {
            'method': 'Credit Card',
            'card': f"****{self.card_number[-4:]}",
            'amount': amount,
            'status': 'success'
        }


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def __call__(self, amount: float) -> dict:
        return {
            'method': 'PayPal',
            'email': self.email,
            'amount': amount,
            'status': 'success'
        }


class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def __call__(self, amount: float) -> dict:
        return {
            'method': 'Cryptocurrency',
            'wallet': self.wallet_address[:10] + "...",
            'amount': amount,
            'status': 'pending'
        }


class PaymentProcessor:
    def process_payment(self, amount: float, strategy: PaymentStrategy):
        """Process payment using given strategy"""
        result = strategy(amount)
        return result


print("=" * 60)
print("Example 2: Payment Strategy Pattern")
print("=" * 60)

processor = PaymentProcessor()

# Different payment methods
cc_payment = CreditCardPayment("1234567890123456")
paypal_payment = PayPalPayment("user@example.com")
crypto_payment = CryptoPayment("0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb")

# Process payments
result1 = processor.process_payment(100.00, cc_payment)
print(f"Payment 1: {result1}")

result2 = processor.process_payment(50.00, paypal_payment)
print(f"Payment 2: {result2}")

result3 = processor.process_payment(200.00, crypto_payment)
print(f"Payment 3: {result3}")
print()


# Example 3: Query Builder with Callable Filters
class QueryFilter:
    """Base class for query filters"""

    def __call__(self, item: dict) -> bool:
        raise NotImplementedError


class GreaterThan(QueryFilter):
    def __init__(self, field: str, value: Any):
        self.field = field
        self.value = value

    def __call__(self, item: dict) -> bool:
        return item.get(self.field, 0) > self.value


class LessThan(QueryFilter):
    def __init__(self, field: str, value: Any):
        self.field = field
        self.value = value

    def __call__(self, item: dict) -> bool:
        return item.get(self.field, 0) < self.value


class Equals(QueryFilter):
    def __init__(self, field: str, value: Any):
        self.field = field
        self.value = value

    def __call__(self, item: dict) -> bool:
        return item.get(self.field) == self.value


class Contains(QueryFilter):
    def __init__(self, field: str, value: str):
        self.field = field
        self.value = value.lower()

    def __call__(self, item: dict) -> bool:
        field_value = str(item.get(self.field, "")).lower()
        return self.value in field_value


class Database:
    def __init__(self, data: List[dict]):
        self.data = data

    def query(self, *filters: QueryFilter) -> List[dict]:
        """Apply filters and return matching items"""
        results = self.data
        for filter_func in filters:
            results = [item for item in results if filter_func(item)]
        return results


print("=" * 60)
print("Example 3: Query Filters")
print("=" * 60)

# Sample data
products = [
    {'id': 1, 'name': 'Laptop', 'price': 999, 'category': 'Electronics'},
    {'id': 2, 'name': 'Mouse', 'price': 29, 'category': 'Electronics'},
    {'id': 3, 'name': 'Desk', 'price': 299, 'category': 'Furniture'},
    {'id': 4, 'name': 'Chair', 'price': 199, 'category': 'Furniture'},
    {'id': 5, 'name': 'Keyboard', 'price': 79, 'category': 'Electronics'},
]

db = Database(products)

# Query: Electronics under $100
print("Electronics under $100:")
results = db.query(
    Equals('category', 'Electronics'),
    LessThan('price', 100)
)
for item in results:
    print(f"  {item['name']}: ${item['price']}")
print()

# Query: Products with 'chair' in name
print("Products containing 'chair':")
results = db.query(Contains('name', 'chair'))
for item in results:
    print(f"  {item['name']}")
print()


# Example 4: Middleware Pipeline
class Middleware:
    """Base middleware class"""

    def __call__(self, request: dict, next_middleware: Callable) -> dict:
        raise NotImplementedError


class LoggingMiddleware(Middleware):
    def __call__(self, request: dict, next_middleware: Callable) -> dict:
        print(
            f"  [LOG] Incoming request: {request['method']} {request['path']}")
        response = next_middleware(request)
        print(f"  [LOG] Response status: {response['status']}")
        return response


class AuthMiddleware(Middleware):
    def __call__(self, request: dict, next_middleware: Callable) -> dict:
        if 'Authorization' not in request['headers']:
            print("  [AUTH] No authorization header")
            return {'status': 401, 'body': 'Unauthorized'}

        print("  [AUTH] Request authorized")
        return next_middleware(request)


class RateLimitMiddleware(Middleware):
    def __init__(self):
        self.request_count = 0
        self.limit = 5

    def __call__(self, request: dict, next_middleware: Callable) -> dict:
        self.request_count += 1
        if self.request_count > self.limit:
            print(f"  [RATE] Request limit exceeded ({self.limit})")
            return {'status': 429, 'body': 'Too Many Requests'}

        print(f"  [RATE] Request {self.request_count}/{self.limit}")
        return next_middleware(request)


class Server:
    def __init__(self):
        self.middlewares = []

    def use(self, middleware: Middleware):
        """Add middleware to pipeline"""
        self.middlewares.append(middleware)

    def handle_request(self, request: dict) -> dict:
        """Process request through middleware pipeline"""
        def run_middleware(index: int, req: dict) -> dict:
            if index >= len(self.middlewares):
                # Final handler
                return {'status': 200, 'body': 'Success'}

            middleware = self.middlewares[index]
            return middleware(req, lambda r: run_middleware(index + 1, r))

        return run_middleware(0, request)


print("=" * 60)
print("Example 4: Middleware Pipeline")
print("=" * 60)

server = Server()
server.use(LoggingMiddleware())
server.use(RateLimitMiddleware())
server.use(AuthMiddleware())

# Request 1 - with auth
print("Request 1:")
response1 = server.handle_request({
    'method': 'GET',
    'path': '/api/users',
    'headers': {'Authorization': 'Bearer token123'}
})
print(f"Result: {response1}")
print()

# Request 2 - without auth
print("Request 2:")
response2 = server.handle_request({
    'method': 'POST',
    'path': '/api/posts',
    'headers': {}
})
print(f"Result: {response2}")
print()


# Example 5: Command Pattern
class Command:
    """Base command class"""

    def __call__(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


class AddCommand(Command):
    def __init__(self, receiver: List, item: Any):
        self.receiver = receiver
        self.item = item

    def __call__(self):
        self.receiver.append(self.item)
        print(f"  Added: {self.item}")

    def undo(self):
        self.receiver.remove(self.item)
        print(f"  Removed: {self.item}")


class RemoveCommand(Command):
    def __init__(self, receiver: List, item: Any):
        self.receiver = receiver
        self.item = item
        self.index = None

    def __call__(self):
        self.index = self.receiver.index(self.item)
        self.receiver.remove(self.item)
        print(f"  Removed: {self.item}")

    def undo(self):
        self.receiver.insert(self.index, self.item)
        print(f"  Restored: {self.item}")


class CommandManager:
    def __init__(self):
        self.history = []

    def execute(self, command: Command):
        """Execute a command and save to history"""
        command()
        self.history.append(command)

    def undo(self):
        """Undo last command"""
        if self.history:
            command = self.history.pop()
            command.undo()


print("=" * 60)
print("Example 5: Command Pattern (Undo/Redo)")
print("=" * 60)

tasks = []
manager = CommandManager()

print("Executing commands:")
manager.execute(AddCommand(tasks, "Task 1"))
manager.execute(AddCommand(tasks, "Task 2"))
manager.execute(AddCommand(tasks, "Task 3"))
print(f"Tasks: {tasks}")
print()

print("Undoing last command:")
manager.undo()
print(f"Tasks: {tasks}")
print()

print("Undoing another command:")
manager.undo()
print(f"Tasks: {tasks}")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. Callables enable flexible design patterns")
print("2. Strategy pattern: swap algorithms at runtime")
print("3. Command pattern: encapsulate actions")
print("4. Middleware: chain processing steps")
print("5. Callbacks: event-driven programming")
print("6. Filters: compose query logic")
