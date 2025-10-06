"""
Holds only Immutable Objects

A set can store only immutable objects such as number (int, float, complex or bool), string or tuple.
If you try to put a list or a dictionary in the set collection, Python raises a TypeError.

Lets check set if it can hold mutable object like list[]

"""

"""
📌 Understanding Hashability and Sets in Python

In Python, sets can only contain **hashable** (immutable) types.

Mutable types like `list`, `dict`, or `set` cannot be added as elements in a set,
because they are not hashable.

Examples:

| Code                             | Description                                          | Valid?       |
|----------------------------------|------------------------------------------------------|--------------|
| set([1, 2, 3])                   | Converts list to set; adds each element individually | ✅ Valid     |
| {1, 2, 3}                        | Direct set declaration with integers                | ✅ Valid     |
| {[1, 2, 3]}                      | Trying to insert a list as a set item               | ❌ Invalid   |
| set({1, 2, 3})                   | Converts set to set (still valid)                   | ✅ Valid     |
| { (1, 2), (3, 4) }               | Tuple is hashable, so allowed as set elements       | ✅ Valid     |
| { [1, 2], (3, 4) }              | List is unhashable, so this throws an error         | ❌ Invalid   |

🔸 Use `set()` when creating a set from an iterable like list or tuple.
🔸 Do **not** try to insert a list directly into a set as an element.

"""


# ❌ Why this fails:
# 👈 You are trying to store a list **as an element** inside a set
my_set = {[123, 452, 5, 6]}
print("my_set = ", my_set)

# Output: TypeError: unhashable type: 'list'

# 👈 You are passing a list to the set constructor to create a set
my_set2 = set([123, 452, 5, 6])

# Here, you're not storing a list inside the set. You're passing a list as an argument to the set() constructor. Python simply takes each element inside that list and stores it individually in the set.
