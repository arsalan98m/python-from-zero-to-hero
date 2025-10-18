"""
Ordering and Comparison in Dataclasses
======================================

order=True automatically generates comparison methods:
__lt__, __le__, __gt__, __ge__
"""

from datetime import datetime
from dataclasses import dataclass, field

# Example 1: Basic Ordering


@dataclass(order=True)
class Student:
    grade: float
    name: str = field(compare=False)  # Don't use name in comparison
    student_id: str = field(compare=False)


print("=" * 60)
print("Example 1: Sorting Students by Grade")
print("=" * 60)

students = [
    Student(85.5, "Alice", "S001"),
    Student(92.0, "Bob", "S002"),
    Student(78.5, "Charlie", "S003"),
    Student(95.5, "Diana", "S004"),
]

print("Original order:")
for s in students:
    print(f"  {s.name}: {s.grade}")
print()

# Sort automatically!
students_sorted = sorted(students)
print("Sorted by grade:")
for s in students_sorted:
    print(f"  {s.name}: {s.grade}")
print()

# Can also use comparison operators
print(f"Bob's grade > Alice's grade: {students[1] > students[0]}")
print()


# Example 2: Product Pricing
@dataclass(order=True)
class Product:
    price: float
    name: str = field(compare=False)
    product_id: int = field(compare=False)


print("=" * 60)
print("Example 2: Sorting Products by Price")
print("=" * 60)

products = [
    Product(999.99, "Laptop", 101),
    Product(29.99, "Mouse", 102),
    Product(79.99, "Keyboard", 103),
    Product(199.99, "Monitor", 104),
]

print("Products sorted by price:")
for p in sorted(products):
    print(f"  {p.name}: ${p.price}")
print()


# Example 3: Priority Task System
@dataclass(order=True)
class Task:
    priority: int  # 1=highest, 5=lowest
    task_id: int = field(compare=False)
    description: str = field(compare=False)
    assigned_to: str = field(compare=False)


print("=" * 60)
print("Example 3: Task Priority Queue")
print("=" * 60)

tasks = [
    Task(3, 101, "Write documentation", "Alice"),
    Task(1, 102, "Fix critical bug", "Bob"),
    Task(2, 103, "Code review", "Charlie"),
    Task(1, 104, "Deploy to production", "Diana"),
    Task(5, 105, "Update README", "Eve"),
]

print("Tasks by priority (1=highest):")
for task in sorted(tasks):
    print(
        f"  Priority {task.priority}: {task.description} ({task.assigned_to})")
print()


# Example 4: Date-based Events


@dataclass(order=True)
class Event:
    date_str: str  # Format: YYYY-MM-DD
    event_id: int = field(compare=False)
    title: str = field(compare=False)
    location: str = field(compare=False)


print("=" * 60)
print("Example 4: Chronological Events")
print("=" * 60)

events = [
    Event("2025-03-15", 1, "Conference", "NYC"),
    Event("2025-01-10", 2, "Workshop", "LA"),
    Event("2025-02-20", 3, "Meetup", "SF"),
    Event("2025-04-05", 4, "Seminar", "Chicago"),
]

print("Events in chronological order:")
for event in sorted(events):
    print(f"  {event.date_str}: {event.title} in {event.location}")
print()


# Example 5: Employee Salary Comparison
@dataclass(order=True)
class Employee:
    salary: float
    employee_id: int = field(compare=False)
    name: str = field(compare=False)
    department: str = field(compare=False)


print("=" * 60)
print("Example 5: Employee Salaries")
print("=" * 60)

employees = [
    Employee(75000, 1, "Alice", "Engineering"),
    Employee(95000, 2, "Bob", "Engineering"),
    Employee(65000, 3, "Charlie", "Marketing"),
    Employee(85000, 4, "Diana", "Sales"),
]

print("Employees sorted by salary (lowest to highest):")
for emp in sorted(employees):
    print(f"  {emp.name}: ${emp.salary:,.2f}")
print()

print("Top earners (highest to lowest):")
for emp in sorted(employees, reverse=True)[:2]:
    print(f"  {emp.name}: ${emp.salary:,.2f}")
print()


# Example 6: Multiple Field Comparison
@dataclass(order=True)
class Score:
    # Comparison uses ALL fields by default (in order)
    points: int
    time_seconds: float  # Used as tiebreaker
    player_name: str = field(compare=False)


print("=" * 60)
print("Example 6: Game Leaderboard with Tiebreaker")
print("=" * 60)

scores = [
    Score(100, 45.2, "Alice"),
    Score(100, 42.8, "Bob"),      # Same points, but faster time
    Score(95, 40.0, "Charlie"),
    Score(100, 50.1, "Diana"),    # Same points, but slower time
]

print("Leaderboard (by points, then by time):")
for i, score in enumerate(sorted(scores, reverse=True), 1):
    print(
        f"  {i}. {score.player_name}: {score.points} points in {score.time_seconds}s")
print()


# Example 7: Custom Sort Key (without order=True)
@dataclass
class Book:
    title: str
    author: str
    year: int
    pages: int


print("=" * 60)
print("Example 7: Custom Sorting (Multiple Ways)")
print("=" * 60)

books = [
    Book("1984", "George Orwell", 1949, 328),
    Book("The Hobbit", "J.R.R. Tolkien", 1937, 310),
    Book("Harry Potter", "J.K. Rowling", 1997, 223),
]

print("Sort by year:")
for book in sorted(books, key=lambda b: b.year):
    print(f"  {book.year}: {book.title}")
print()

print("Sort by pages:")
for book in sorted(books, key=lambda b: b.pages):
    print(f"  {book.pages} pages: {book.title}")
print()

print("Sort by author:")
for book in sorted(books, key=lambda b: b.author):
    print(f"  {book.author}: {book.title}")
print()


# Example 8: Finding Min/Max
@dataclass(order=True)
class Temperature:
    celsius: float
    city: str = field(compare=False)
    date: str = field(compare=False)


print("=" * 60)
print("Example 8: Finding Extremes")
print("=" * 60)

temps = [
    Temperature(25.5, "New York", "2025-01-01"),
    Temperature(18.0, "London", "2025-01-01"),
    Temperature(32.0, "Dubai", "2025-01-01"),
    Temperature(-5.0, "Moscow", "2025-01-01"),
]

hottest = max(temps)
coldest = min(temps)

print(f"Hottest: {hottest.city} at {hottest.celsius}°C")
print(f"Coldest: {coldest.city} at {coldest.celsius}°C")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. order=True enables sorting and comparison (<, >, <=, >=)")
print("2. First field is primary sort key by default")
print("3. Use field(compare=False) to exclude fields from comparison")
print("4. Can use sorted(), min(), max() functions")
print("5. Multiple fields used in order for tiebreaking")
print("6. Alternative: use key parameter in sorted()")
