"""
🔗 Chained Comparison Operators in Python
Chained comparison operators allow you to combine multiple comparisons in a 
more concise and readable way — just like how you'd write them in plain math.

"""

# ✅ Instead of writing:
x = 5
if x > 3 and x < 10:
    print("x is between 3 and 10")


# ✅ You can write:
if 3 < x < 10:
    print("x is between 3 and 10")

"""
🧠 How It Works:

Python evaluates chained comparisons like:

a < b < c

AS:

a < b and b < c

This means each comparison is evaluated from left to right, and all conditions
must be true.

x = 7

print(3 < x < 10)      # True
print(3 < x < 5)       # False
print(1 == x < 10)     # False (1 == x is False)
print(7 == x < 10)     # True (7 == x AND x < 10)

"""
