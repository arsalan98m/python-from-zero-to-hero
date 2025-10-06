"""
copy() Method
The .copy() method creates a shallow copy of the list (a new list with the same items).

- If the elements are simple types (like strings, numbers):
  It works just like a full copy — no problem at all.

- But if the list contains nested objects (like other lists), the inner objects are not
  copied — both lists will still point to the same inner objects.


🔁 So what to do for full copy?
Use deepcopy() from the copy module
"""

# 📌 Example 1: Shallow copy with simple values (strings, numbers)
fruits = ["apple", "banana", "cherry"]
copy_fruits = fruits.copy()

# ✅ Changes in copy_fruits did not affect fruits — because elements are strings (simple types).
copy_fruits[0] = "orange"
print("Original:", fruits)
print("Copy:", copy_fruits)


# 📌 Example 2: Shallow copy with nested list(reference issue)
nested = [[1, 2], [3, 4]]
copy_nested = nested.copy()

# ❌ This changes both lists because nested lists are references.
# ⚠️ Both lists got changed — because they share the same inner list ([1, 2]) due to shallow copying.
copy_nested[0][0] = 999
print("Original:", nested)
print("Copy:", copy_nested)
