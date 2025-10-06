"""
Accessing Values

You can access the value associated with a key using square brackets [] or the get() method.
"""

person: dict = {
    "name": "Arsalan",
    "age": 25,
    "visited_cities": ["Lahore", "Karachi", "Islamabad"],
}


print(person["name"])  # Output: Arsalan
# print(person["gender"])  # ❌ This will raise KeyError: 'gender'

# 📌 Accessing Values with get()
print(person.get("age"))  # Output: 25
print(person.get("gender"))  # Output: None

# 📌 Accessing Values with get() and Default Value
print(person.get("gender", "Gender not found"))  # Output: Gender not found
