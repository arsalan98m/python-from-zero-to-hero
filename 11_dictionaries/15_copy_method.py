"""
copy() -> dict

Returns a shallow copy of the dictionary.

- A **shallow copy** means it copies the outer dictionary structure, 
  but **not the nested objects inside it**.
- Changes made to mutable nested objects (like lists or other dicts) 
  will reflect in both the original and copied dictionaries.

Useful when:
- You want to work with a copy of a dictionary without affecting the original.
- But you don't want a deep, fully independent clone of all nested objects.

Example:
original = {'a': 1, 'b': [2, 3]}
copy_dict = original.copy()
copy_dict['b'].append(4)
print(original)     # {'a': 1, 'b': [2, 3, 4]}
print(copy_dict)    # {'a': 1, 'b': [2, 3, 4]}

 
"""

import copy

# Original dictionary with a nested list
original = {
    "name": "Arsalan",
    "scores": [85, 90, 95]
}

# Create a shallow copy using dict.copy()
copied = original.copy()

# Modify the nested list in the copied dictionary
copied["scores"].append(100)

# Both original and copied dict reflect the change in the nested list
print("Original:", original)
print("Copied:  ", copied)

# Output:
# Original: {'name': 'Arsalan', 'scores': [85, 90, 95, 100]}
# Copied:   {'name': 'Arsalan', 'scores': [85, 90, 95, 100]}

"""
⚠️ Why this happens?
Because .copy() only creates a shallow copy — it does not duplicate nested objects
like lists. Both original["scores"] and copied["scores"] point to the same list in 
memory.

✅ Want a full independent copy?

Use copy.deepcopy() if you want true independence:
"""


deep_copied = copy.deepcopy(original)
deep_copied["scores"].append(200)

print("Original after deepcopy:", original)
print("Deep Copied:            ", deep_copied)

# Output:
# Original after deepcopy: {'name': 'Arsalan', 'scores': [85, 90, 95, 100]}
# Deep Copied:             {'name': 'Arsalan', 'scores': [85, 90, 95, 100, 200]}
