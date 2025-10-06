person: dict = {
    "name": "Arsalan",
    "age": 25,
    "visited_cities": ["Lahore", "Karachi", "Islamabad"],
}

last_item = person.popitem()  # Removes and returns the last item as a tuple
# ('visited_cities', ['Lahore', 'Karachi', 'Islamabad'])
print("last_item: ", last_item)
print("person: ", person)  # {'name': 'Arsalan', 'age': 25}
