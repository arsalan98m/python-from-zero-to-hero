"""
index() Method

- The .index(value) method returns the first index where the value appears.
- Raises ValueError if not found.
"""

fruits = ["apple", "banana", "cherry", "banana"]

index = fruits.index("banana")

print("Index of 'banana': ", index)

# index = fruits.index("orange")  # ❌ this will raise ValueError 'orange' is not in the list
