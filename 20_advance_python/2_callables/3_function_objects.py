"""
Functions as First-Class Objects
================================

In Python, functions are first-class objects:
- Can be assigned to variables
- Can be passed as arguments
- Can be returned from other functions
- Can be stored in data structures
"""

# Example 1: Functions assigned to variables


def greet(name):
    return f"Hello, {name}!"


def farewell(name):
    return f"Goodbye, {name}!"


print("=" * 60)
print("Example 1: Functions as Variables")
print("=" * 60)

# Assign function to variable
say_hello = greet
say_bye = farewell

print(say_hello("Alice"))
print(say_bye("Bob"))

# The variable holds a reference to the function
print(f"greet function: {greet}")
print(f"say_hello variable: {say_hello}")
print(f"Same function? {say_hello is greet}")
print()


# Example 2: Functions in data structures
print("=" * 60)
print("Example 2: Functions in Lists/Dicts")
print("=" * 60)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"


# Store functions in a list
operations = [add, subtract, multiply, divide]

print("Applying operations to (10, 5):")
for op in operations:
    result = op(10, 5)
    print(f"  {op.__name__}(10, 5) = {result}")
print()

# Store functions in a dictionary
calculator = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print("Calculator dictionary:")
print(f"10 + 5 = {calculator['+'](10, 5)}")
print(f"10 - 5 = {calculator['-'](10, 5)}")
print(f"10 * 5 = {calculator['*'](10, 5)}")
print(f"10 / 5 = {calculator['/'](10, 5)}")
print()


# Example 3: Functions as arguments (Higher-order functions)
def apply_operation(func, x, y):
    """Apply any function to x and y"""
    return func(x, y)


print("=" * 60)
print("Example 3: Functions as Arguments")
print("=" * 60)

result1 = apply_operation(add, 15, 5)
result2 = apply_operation(multiply, 15, 5)

print(f"apply_operation(add, 15, 5) = {result1}")
print(f"apply_operation(multiply, 15, 5) = {result2}")
print()


# Example 4: Real-world - Data Processing Pipeline
def uppercase(text):
    return text.upper()


def remove_spaces(text):
    return text.replace(" ", "")


def add_exclamation(text):
    return text + "!"


def process_text(text, *functions):
    """Apply a series of functions to text"""
    result = text
    for func in functions:
        result = func(result)
    return result


print("=" * 60)
print("Example 4: Data Processing Pipeline")
print("=" * 60)

text = "hello world"
print(f"Original: {text}")

result = process_text(text, uppercase, remove_spaces, add_exclamation)
print(f"Processed: {result}")
print()


# Example 5: Returning functions from functions
def make_multiplier(factor):
    """Return a function that multiplies by factor"""
    def multiplier(x):
        return x * factor
    return multiplier


print("=" * 60)
print("Example 5: Functions Returning Functions")
print("=" * 60)

double = make_multiplier(2)
triple = make_multiplier(3)
times_ten = make_multiplier(10)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")
print(f"times_ten(5) = {times_ten(5)}")
print()


# Example 6: Real-world - Greeting Factory
def make_greeter(greeting, punctuation="!"):
    """Create a customized greeting function"""
    def greet(name):
        return f"{greeting}, {name}{punctuation}"
    return greet


print("=" * 60)
print("Example 6: Greeting Factory")
print("=" * 60)

casual = make_greeter("Hey")
formal = make_greeter("Good evening", ".")
excited = make_greeter("HELLO", "!!!")

print(casual("Alice"))
print(formal("Mr. Smith"))
print(excited("Everyone"))
print()


# Example 7: Real-world - Validator Factory
def make_range_validator(min_val, max_val):
    """Create a validator for a specific range"""
    def validate(value):
        return min_val <= value <= max_val
    return validate


print("=" * 60)
print("Example 7: Validator Factory")
print("=" * 60)

age_validator = make_range_validator(18, 100)
percentage_validator = make_range_validator(0, 100)
temperature_validator = make_range_validator(-50, 50)

print("Validate age (18-100):")
print(f"  25: {age_validator(25)}")
print(f"  15: {age_validator(15)}")
print()

print("Validate percentage (0-100):")
print(f"  85: {percentage_validator(85)}")
print(f"  150: {percentage_validator(150)}")
print()


# Example 8: Built-in higher-order functions
print("=" * 60)
print("Example 8: Built-in Higher-Order Functions")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

# map() - applies function to each element
squared = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")
print()

# filter() - keeps elements where function returns True
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even}")
print()

# sorted() with key function
words = ["apple", "pie", "zoo", "a"]
sorted_by_length = sorted(words, key=len)
print(f"Words: {words}")
print(f"Sorted by length: {sorted_by_length}")
print()


# Example 9: Real-world - Discount Strategy
def no_discount(price):
    return price


def ten_percent_off(price):
    return price * 0.9


def twenty_percent_off(price):
    return price * 0.8


def buy_one_get_half_off(price):
    return price * 1.5  # Assuming 2 items


class PriceCalculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, price):
        return round(self.strategy(price), 2)

    def change_strategy(self, new_strategy):
        self.strategy = new_strategy


print("=" * 60)
print("Example 9: Pricing Strategy Pattern")
print("=" * 60)

calculator = PriceCalculator(no_discount)
print(f"No discount: ${calculator.calculate(100)}")

calculator.change_strategy(ten_percent_off)
print(f"10% off: ${calculator.calculate(100)}")

calculator.change_strategy(twenty_percent_off)
print(f"20% off: ${calculator.calculate(100)}")
print()


# Example 10: Closure (function remembering its environment)
def make_counter(start=0):
    """Create a counter function with enclosed state"""
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


print("=" * 60)
print("Example 10: Closures")
print("=" * 60)

counter1 = make_counter(0)
counter2 = make_counter(100)

print("Counter 1:")
print(f"  {counter1()}, {counter1()}, {counter1()}")

print("Counter 2:")
print(f"  {counter2()}, {counter2()}, {counter2()}")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. Functions are objects in Python")
print("2. Can assign functions to variables")
print("3. Can store functions in lists/dicts")
print("4. Can pass functions as arguments")
print("5. Can return functions from functions")
print("6. Enables powerful patterns (callbacks, strategies)")
print("7. Built-in functions like map/filter use this")
