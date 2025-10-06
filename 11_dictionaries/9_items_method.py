"""
Dictionaries provide a method called items() that returns a view of the key-value pairs as tuples.

The syntax is:
dictionary.items()

"""

person: dict = {
    "name": "Arsalan",
    "age": 25,
    "visited_cities": ["Lahore", "Karachi", "Islamabad"],
}

print("person.items(): ", person.items())
