"""
Creating a Dictionary

Dictionaries are created using curly braces {} with key-value pairs separated by commas.

The syntax is:
dictionary = {key1: value1, key2: value2, ...}
"""


# 📌 Creating a Dictionary
person: dict = {
    "name": "Arsalan",
    "age": 25,
    "visited_cities": ["Lahore", "Karachi", "Islamabad"],
}

print("type(person): ", type(person))
print("person: ", person)

# 📌 Creating a Dictionary with dict()
person_2: dict = dict(
    name="Arsalan",
    age=25,
    visited_cities=["Lahore", "Karachi", "Islamabad"],
)

print("type(person_2): ", type(person_2))
print("person_2: ", person_2)
