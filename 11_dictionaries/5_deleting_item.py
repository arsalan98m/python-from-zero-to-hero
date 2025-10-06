"""
del dict[key]

Deletes the specified key and its value from the dictionary.
If the key does not exist, it raises a KeyError.

Usage:
- Used to delete a specific key-value pair permanently.
- Cannot be used to safely remove a key like pop (no default fallback).

Example:
person = {'name': 'Ali', 'age': 30}
del person['age']  # Deletes the key 'age'
"""

"""
pop(key[, default]) -> value (key is required, default is optional)

Removes the specified key from the dictionary and returns its value.
If the key is not found and a default value is provided, the default is returned.
If the key is not found and no default is provided, it raises a KeyError.

Usage:
- Safe way to remove an item and get its value.
- Can optionally handle missing keys without throwing an error.

Example:
person = {'name': 'Ali', 'age': 30}
age = person.pop('age')  # Removes 'age' and returns 30
"""


person: dict = {
    "name": "Arsalan",
    "age": 25,
    "visited_cities": ["Lahore", "Karachi", "Islamabad"],
}

# Remove a key-value pair using del
del person["age"]
print("person: ", person)

# del person["gender"]  # ❌ This will raise KeyError: 'gender'

# Remove a key-value pair using pop()
removed_value = person.pop("visited_cities")
print("removed_value: ", removed_value)
print("person: ", person)

# Remove a key-value pair using pop() with a default value
removed_value = person.pop("gender", "Gender not found")
print("removed_value: ", removed_value)
print("person: ", person)
