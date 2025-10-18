"""
Generic Classes
===============

Creating classes that work with any type while maintaining type safety
"""

from typing import TypeVar, Generic, List, Optional, Dict

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

# Example 1: Basic Generic Class
print("=" * 60)
print("Example 1: Basic Generic Stack")
print("=" * 60)


class Stack(Generic[T]):
    """Generic stack that works with any type"""

    def __init__(self):
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Add item to stack"""
        self._items.append(item)

    def pop(self) -> Optional[T]:
        """Remove and return top item"""
        return self._items.pop() if self._items else None

    def peek(self) -> Optional[T]:
        """View top item without removing"""
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        """Check if stack is empty"""
        return len(self._items) == 0

    def size(self) -> int:
        """Get stack size"""
        return len(self._items)


# Use with integers
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)

print("Integer Stack:")
print(f"  Top: {int_stack.peek()}")
print(f"  Popped: {int_stack.pop()}")
print(f"  Size: {int_stack.size()}")
print()

# Use with strings
str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")

print("String Stack:")
print(f"  Top: {str_stack.peek()}")
print(f"  Popped: {str_stack.pop()}")
print()


# Example 2: Generic Queue
print("=" * 60)
print("Example 2: Generic Queue")
print("=" * 60)


class Queue(Generic[T]):
    """Generic FIFO queue"""

    def __init__(self):
        self._items: List[T] = []

    def enqueue(self, item: T) -> None:
        """Add item to back of queue"""
        self._items.append(item)

    def dequeue(self) -> Optional[T]:
        """Remove and return front item"""
        return self._items.pop(0) if self._items else None

    def front(self) -> Optional[T]:
        """View front item"""
        return self._items[0] if self._items else None

    def is_empty(self) -> bool:
        """Check if queue is empty"""
        return len(self._items) == 0


# Task queue
task_queue: Queue[str] = Queue()
task_queue.enqueue("Task 1")
task_queue.enqueue("Task 2")
task_queue.enqueue("Task 3")

print("Task Queue:")
while not task_queue.is_empty():
    print(f"  Processing: {task_queue.dequeue()}")
print()


# Example 3: Generic Box Container
print("=" * 60)
print("Example 3: Generic Box Container")
print("=" * 60)


class Box(Generic[T]):
    """Container that holds a single value"""

    def __init__(self, content: T):
        self._content = content

    def get(self) -> T:
        """Get the content"""
        return self._content

    def set(self, content: T) -> None:
        """Set new content"""
        self._content = content

    def transform(self, func) -> 'Box[T]':
        """Transform content and return new Box"""
        return Box(func(self._content))


int_box: Box[int] = Box(42)
print(f"Integer box: {int_box.get()}")

str_box: Box[str] = Box("hello")
print(f"String box: {str_box.get()}")

# Transform
doubled_box = int_box.transform(lambda x: x * 2)
print(f"Doubled: {doubled_box.get()}")

upper_box = str_box.transform(lambda x: x.upper())
print(f"Uppercase: {upper_box.get()}")
print()


# Example 4: Generic Pair with Two Types
print("=" * 60)
print("Example 4: Generic Pair (Two Type Parameters)")
print("=" * 60)


class Pair(Generic[K, V]):
    """Pair with two potentially different types"""

    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value

    def get_key(self) -> K:
        return self.key

    def get_value(self) -> V:
        return self.value

    def swap(self) -> 'Pair[V, K]':
        """Return new pair with key and value swapped"""
        return Pair(self.value, self.key)


# String to Int
pair1: Pair[str, int] = Pair("age", 30)
print(f"Pair 1: {pair1.get_key()} = {pair1.get_value()}")

# Int to String
pair2: Pair[int, str] = Pair(1, "first")
print(f"Pair 2: {pair2.get_key()} = {pair2.get_value()}")

# Swap types
swapped = pair1.swap()  # Now Pair[int, str]
print(f"Swapped: {swapped.get_key()} = {swapped.get_value()}")
print()


# Example 5: Real-world - Generic Repository
print("=" * 60)
print("Example 5: Generic Repository Pattern")
print("=" * 60)


class Repository(Generic[T]):
    """Generic repository for storing items"""

    def __init__(self):
        self._items: Dict[int, T] = {}
        self._next_id = 1

    def add(self, item: T) -> int:
        """Add item and return its ID"""
        item_id = self._next_id
        self._items[item_id] = item
        self._next_id += 1
        return item_id

    def get(self, item_id: int) -> Optional[T]:
        """Get item by ID"""
        return self._items.get(item_id)

    def get_all(self) -> List[T]:
        """Get all items"""
        return list(self._items.values())

    def delete(self, item_id: int) -> bool:
        """Delete item by ID"""
        if item_id in self._items:
            del self._items[item_id]
            return True
        return False

    def count(self) -> int:
        """Count total items"""
        return len(self._items)


class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"


# User repository
user_repo: Repository[User] = Repository()

id1 = user_repo.add(User("Alice", "alice@example.com"))
id2 = user_repo.add(User("Bob", "bob@example.com"))
id3 = user_repo.add(User("Charlie", "charlie@example.com"))

print("User Repository:")
print(f"  Total users: {user_repo.count()}")
print(f"  User {id1}: {user_repo.get(id1)}")
print(f"  All users: {user_repo.get_all()}")
print()


# Example 6: Generic Result Type (Success/Error)
print("=" * 60)
print("Example 6: Generic Result Type")
print("=" * 60)


class Result(Generic[T]):
    """Represent success or failure"""

    def __init__(self, value: Optional[T] = None, error: Optional[str] = None):
        self._value = value
        self._error = error

    def is_success(self) -> bool:
        """Check if result is successful"""
        return self._error is None

    def get_value(self) -> Optional[T]:
        """Get value if successful"""
        return self._value

    def get_error(self) -> Optional[str]:
        """Get error message if failed"""
        return self._error

    @staticmethod
    def success(value: T) -> 'Result[T]':
        """Create successful result"""
        return Result(value=value)

    @staticmethod
    def failure(error: str) -> 'Result[T]':
        """Create failed result"""
        return Result(error=error)


def divide(a: float, b: float) -> Result[float]:
    """Divide two numbers, returning Result"""
    if b == 0:
        return Result.failure("Division by zero")
    return Result.success(a / b)


result1 = divide(10, 2)
result2 = divide(10, 0)

print("Division Results:")
if result1.is_success():
    print(f"  10 / 2 = {result1.get_value()}")
else:
    print(f"  Error: {result1.get_error()}")

if result2.is_success():
    print(f"  10 / 0 = {result2.get_value()}")
else:
    print(f"  Error: {result2.get_error()}")
print()


# Example 7: Generic Cache
print("=" * 60)
print("Example 7: Generic Cache with Key-Value")
print("=" * 60)


class Cache(Generic[K, V]):
    """Generic cache with key-value pairs"""

    def __init__(self, max_size: int = 100):
        self._data: Dict[K, V] = {}
        self._max_size = max_size

    def set(self, key: K, value: V) -> None:
        """Store value"""
        if len(self._data) >= self._max_size:
            # Remove oldest (in real cache, use LRU)
            first_key = next(iter(self._data))
            del self._data[first_key]
        self._data[key] = value

    def get(self, key: K) -> Optional[V]:
        """Get value"""
        return self._data.get(key)

    def has(self, key: K) -> bool:
        """Check if key exists"""
        return key in self._data

    def clear(self) -> None:
        """Clear all entries"""
        self._data.clear()


# String to Integer cache
cache: Cache[str, int] = Cache(max_size=5)
cache.set("user_1", 100)
cache.set("user_2", 200)
cache.set("user_3", 300)

print("Cache contents:")
print(f"  user_1: {cache.get('user_1')}")
print(f"  user_2: {cache.get('user_2')}")
print(f"  Has user_4? {cache.has('user_4')}")
print()


# Example 8: Generic Node for Linked List
print("=" * 60)
print("Example 8: Generic Linked List Node")
print("=" * 60)


class Node(Generic[T]):
    """Generic node for linked list"""

    def __init__(self, value: T):
        self.value = value
        self.next: Optional[Node[T]] = None


class LinkedList(Generic[T]):
    """Generic linked list"""

    def __init__(self):
        self.head: Optional[Node[T]] = None

    def append(self, value: T) -> None:
        """Add value to end"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self) -> List[T]:
        """Convert to regular list"""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


# Integer linked list
int_list: LinkedList[int] = LinkedList()
int_list.append(1)
int_list.append(2)
int_list.append(3)

print(f"Integer linked list: {int_list.to_list()}")

# String linked list
str_list: LinkedList[str] = LinkedList()
str_list.append("a")
str_list.append("b")
str_list.append("c")

print(f"String linked list: {str_list.to_list()}")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. Generic classes use Generic[T] base class")
print("2. Type parameter specified when creating instance")
print("3. Can have multiple type parameters: Generic[K, V]")
print("4. Methods use the type parameters for type safety")
print("5. Great for containers, repositories, results")
