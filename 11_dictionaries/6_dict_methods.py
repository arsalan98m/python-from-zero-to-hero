"""
📘 Dictionary Methods in Python

Dictionaries provide various built-in methods to make key-value management efficient and easy.

1. keys()
   - Returns a view of all keys in the dictionary.
   - Example: `dict.keys()`

2. values()
   - Returns a view of all values in the dictionary.
   - Example: `dict.values()`

3. items()
   - Returns a view of key-value pairs as (key, value) tuples.
   - Example: `dict.items()`

4. get(key, default=None)
   - Returns the value for the specified key.
   - If the key is not found, returns the default value instead of raising an error.
   - Example: `dict.get("name", "Unknown")`

5. update(other_dict)
   - Adds or updates multiple key-value pairs from another dictionary or iterable of key-value pairs.
   - Example: `dict.update({"age": 25})`

6. pop(key, default)
   - Removes the specified key and returns its value.
   - If key is not found, returns default if provided, else raises KeyError.
   - Example: `dict.pop("age", "Not Found")`

7. popitem()
   - Removes and returns the last inserted key-value pair as a tuple.
   - Example: `dict.popitem()`

8. clear()
   - Removes all items from the dictionary, making it empty.
   - Example: `dict.clear()`

9. setdefault(key, default=None)
   - Returns the value of the key if it exists.
   - If not, inserts the key with the default value and returns default.
   - Example: `dict.setdefault("gender", "unknown")`

These methods help in safely accessing, updating, and cleaning dictionaries in a Pythonic way.
"""
