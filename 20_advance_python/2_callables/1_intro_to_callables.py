"""
Introduction to Callables
=========================

What is a Callable?
- A callable is any object that can be called using parentheses ()
- If you can use object(), then object is callable
- Python has a built-in function callable() to check if something is callable
"""

# Example 1: Functions are callables


def greet(name):
    """A simple function"""
    return f"Hello, {name}!"


print("=" * 60)
print("Example 1: Functions are Callables")
print("=" * 60)

# Call the function
result = greet("Alice")
print(result)

# Check if it's callable
print(f"Is greet callable? {callable(greet)}")
print()


# Example 2: Built-in functions are callables
print("=" * 60)
print("Example 2: Built-in Functions")
print("=" * 60)

print(f"Is print callable? {callable(print)}")
print(f"Is len callable? {callable(len)}")
print(f"Is max callable? {callable(max)}")
print()


# Example 3: Classes are callables (calling them creates instances)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


print("=" * 60)
print("Example 3: Classes are Callables")
print("=" * 60)

print(f"Is Person class callable? {callable(Person)}")

# Calling the class creates an instance
person = Person("Bob", 30)
print(f"Created: {person.name}, age {person.age}")

# But the instance is NOT callable (by default)
print(f"Is person instance callable? {callable(person)}")
print()


# Example 4: Lambda functions are callables
print("=" * 60)
print("Example 4: Lambda Functions")
print("=" * 60)


def square(x): return x ** 2


print(f"Is lambda callable? {callable(square)}")
print(f"square(5) = {square(5)}")
print()


# Example 5: Methods are callables
class Calculator:
    def add(self, a, b):
        return a + b


print("=" * 60)
print("Example 5: Methods are Callables")
print("=" * 60)

calc = Calculator()
print(f"Is calc.add callable? {callable(calc.add)}")
print(f"calc.add(3, 5) = {calc.add(3, 5)}")
print()


# Example 6: NOT everything is callable
print("=" * 60)
print("Example 6: Non-Callable Objects")
print("=" * 60)

number = 42
text = "hello"
my_list = [1, 2, 3]

print(f"Is 42 callable? {callable(number)}")
print(f"Is 'hello' callable? {callable(text)}")
print(f"Is [1,2,3] callable? {callable(my_list)}")

# Trying to call them would cause an error
try:
    number()  # This will fail!
except TypeError as e:
    print(f"Error calling number: {e}")
print()


# Example 7: Making objects callable with __call__
class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        """This method makes instances callable!"""
        return f"{self.greeting}, {name}!"


print("=" * 60)
print("Example 7: Custom Callable Objects")
print("=" * 60)

hello = Greeter("Hello")
print(f"Is hello instance callable? {callable(hello)}")

# Now we can call the instance like a function!
print(hello("Alice"))
print(hello("Bob"))

# Create different greeter
bye = Greeter("Goodbye")
print(bye("Charlie"))
print()


# Example 8: Real-world comparison
print("=" * 60)
print("Summary: What's Callable?")
print("=" * 60)

items = [
    ("Function", greet),
    ("Built-in", print),
    ("Class", Person),
    ("Lambda", lambda x: x),
    ("Method", calc.add),
    ("Callable instance", hello),
    ("Integer", 42),
    ("String", "hello"),
    ("List", [1, 2, 3]),
]

for name, item in items:
    status = "✓ Callable" if callable(item) else "✗ Not callable"
    print(f"{name:20} {status}")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. Callables are objects you can call with ()")
print("2. Functions, methods, classes, and lambdas are callable")
print("3. Regular objects (numbers, strings, lists) are NOT callable")
print("4. Use __call__ method to make custom objects callable")
print("5. Use callable() function to check if something is callable")
