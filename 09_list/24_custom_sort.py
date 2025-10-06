# Custom Sort with Lambda (Case-Insensitive)

words = ["Banana", "apple", "Cherry"]

words.sort(key=lambda x: x.lower())

print("Case-insensitive sort:", words)  # Output: ['apple', 'Banana', 'Cherry']

#  Sorting List of Tuples by Second Item
items = [(1, 3), (2, 1), (4, 2)]
items.sort(key=lambda x: x[1])
print("Sorted by second item:", items)  # Output: [(2, 1), (4, 2), (1, 3)]
