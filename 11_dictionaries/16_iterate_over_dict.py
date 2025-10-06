person: dict = {
    "name": "Arsalan",
    "age": 25,
    "visited_cities": ["Lahore", "Karachi", "Islamabad"],
}

# this will iterate over the keys
for item in person:
    print(item)

# this will iterate over the values
for item in person.values():
    print(item)

# this will iterate over the keys and values
for key, value in person.items():
    print(key, value)
