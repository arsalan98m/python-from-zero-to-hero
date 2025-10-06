# You can add new key-value pairs or modify existing ones.
person: dict = {
    "name": "Arsalan",
    "age": 25,
    "visited_cities": ["Lahore", "Karachi", "Islamabad"],
}

print("person: ", person)

# 📌 Modifying Dictionary
person["age"] = 26
print("person: ", person)

# 📌 Adding New Key-Value Pair
person["gender"] = "Male"
print("person: ", person)
