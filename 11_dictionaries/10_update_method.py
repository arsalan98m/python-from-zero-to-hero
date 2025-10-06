person: dict = {
    "name": "Arsalan",
    "age": 25,
    "visited_cities": ["Lahore", "Karachi", "Islamabad"],
}

# If the key is not found, it will be added to the dictionary
person.update({"gender": "Male"})
print("person: ", person)

person.update({"age": 26, "visited_cities": [
              "Lahore", "Karachi", "Islamabad", "Peshawar"]})
print("person: ", person)
