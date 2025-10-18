"""
The __call__ Method
==================

The __call__ method makes instances of a class callable
When you call an instance, Python automatically calls __call__
"""

# Example 1: Basic __call__ implementation


class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        """Called when instance is called like a function"""
        self.count += 1
        return self.count


print("=" * 60)
print("Example 1: Simple Counter")
print("=" * 60)

counter = Counter()
print(f"First call: {counter()}")
print(f"Second call: {counter()}")
print(f"Third call: {counter()}")
print(f"Current count: {counter.count}")
print()


# Example 2: __call__ with parameters
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        """Multiply value by the stored factor"""
        return value * self.factor


print("=" * 60)
print("Example 2: Multiplier")
print("=" * 60)

double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5) = {double(5)}")
print(f"double(10) = {double(10)}")
print(f"triple(5) = {triple(5)}")
print(f"triple(10) = {triple(10)}")
print()


# Example 3: Real-world - Temperature Converter
class TemperatureConverter:
    def __init__(self, from_unit, to_unit):
        self.from_unit = from_unit.upper()
        self.to_unit = to_unit.upper()

    def __call__(self, temperature):
        """Convert temperature from one unit to another"""
        # First convert to Celsius
        if self.from_unit == "F":
            celsius = (temperature - 32) * 5/9
        elif self.from_unit == "K":
            celsius = temperature - 273.15
        else:  # Already Celsius
            celsius = temperature

        # Then convert to target unit
        if self.to_unit == "F":
            result = celsius * 9/5 + 32
        elif self.to_unit == "K":
            result = celsius + 273.15
        else:  # To Celsius
            result = celsius

        return round(result, 2)


print("=" * 60)
print("Example 3: Temperature Converter")
print("=" * 60)

celsius_to_fahrenheit = TemperatureConverter("C", "F")
fahrenheit_to_celsius = TemperatureConverter("F", "C")
celsius_to_kelvin = TemperatureConverter("C", "K")

print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")
print(f"32°F = {fahrenheit_to_celsius(32)}°C")
print(f"0°C = {celsius_to_kelvin(0)}K")
print()


# Example 4: Real-world - Discount Calculator
class DiscountCalculator:
    def __init__(self, discount_percent):
        self.discount_percent = discount_percent

    def __call__(self, price):
        """Apply discount to price"""
        discount_amount = price * (self.discount_percent / 100)
        final_price = price - discount_amount
        return {
            'original_price': price,
            'discount_percent': self.discount_percent,
            'discount_amount': round(discount_amount, 2),
            'final_price': round(final_price, 2),
            'savings': round(discount_amount, 2)
        }

    def __repr__(self):
        return f"DiscountCalculator({self.discount_percent}%)"


print("=" * 60)
print("Example 4: Discount Calculator")
print("=" * 60)

black_friday = DiscountCalculator(25)
clearance = DiscountCalculator(50)

item1 = black_friday(100)
print(f"Black Friday (25% off):")
print(f"  Original: ${item1['original_price']}")
print(f"  Discount: ${item1['discount_amount']}")
print(f"  Final: ${item1['final_price']}")
print()

item2 = clearance(100)
print(f"Clearance Sale (50% off):")
print(f"  Original: ${item2['original_price']}")
print(f"  Final: ${item2['final_price']}")
print()


# Example 5: Validator (Check if data meets criteria)
class EmailValidator:
    def __call__(self, email):
        """Validate email address"""
        if not isinstance(email, str):
            return False
        if "@" not in email:
            return False
        if "." not in email.split("@")[1]:
            return False
        if len(email) < 5:
            return False
        return True


class AgeValidator:
    def __init__(self, min_age, max_age):
        self.min_age = min_age
        self.max_age = max_age

    def __call__(self, age):
        """Validate age is within range"""
        return self.min_age <= age <= self.max_age


print("=" * 60)
print("Example 5: Validators")
print("=" * 60)

email_validator = EmailValidator()
age_validator = AgeValidator(18, 100)

# Test emails
emails = ["john@example.com", "invalid", "test@domain.co"]
print("Email validation:")
for email in emails:
    status = "✓ Valid" if email_validator(email) else "✗ Invalid"
    print(f"  {email:20} {status}")
print()

# Test ages
ages = [15, 25, 150]
print("Age validation (18-100):")
for age in ages:
    status = "✓ Valid" if age_validator(age) else "✗ Invalid"
    print(f"  Age {age:3} {status}")
print()


# Example 6: Stateful callable (Accumulator)
class Accumulator:
    def __init__(self, initial_value=0):
        self.total = initial_value

    def __call__(self, value):
        """Add value to total and return new total"""
        self.total += value
        return self.total

    def reset(self):
        """Reset accumulator to zero"""
        self.total = 0


print("=" * 60)
print("Example 6: Accumulator (Stateful)")
print("=" * 60)

acc = Accumulator(0)
print(f"Start: {acc.total}")
print(f"Add 10: {acc(10)}")
print(f"Add 20: {acc(20)}")
print(f"Add 5: {acc(5)}")
print(f"Final total: {acc.total}")

acc.reset()
print(f"After reset: {acc.total}")
print()


# Example 7: Decorator as callable
class Logger:
    def __init__(self, func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        """Log function calls"""
        self.call_count += 1
        print(f"[LOG] Call #{self.call_count} to {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"[LOG] {self.func.__name__} returned: {result}")
        return result


print("=" * 60)
print("Example 7: Callable as Decorator")
print("=" * 60)


@Logger
def add(a, b):
    return a + b


result1 = add(5, 3)
result2 = add(10, 20)
print(f"\nTotal calls to add: {add.call_count}")
print()


print("=" * 60)
print("Key Takeaways:")
print("=" * 60)
print("1. __call__ makes instances callable like functions")
print("2. Useful for creating configurable functions")
print("3. Great for validators, converters, calculators")
print("4. Can maintain state between calls")
print("5. Can accept any parameters like regular functions")
