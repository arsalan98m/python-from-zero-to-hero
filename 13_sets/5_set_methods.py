"""
Set Methods and Properties in Python
------------------------------------

A set is an unordered, unindexed collection of unique elements. It is mutable, meaning items can be added or removed.

Python provides several built-in methods to work with sets:

Basic Methods:
- add(elem): Adds a single element to the set.
- update(iterable): Adds multiple elements from another iterable.
- remove(elem): Removes the specified element. Raises KeyError if not found.
- discard(elem): Removes the specified element. Does not raise an error if not found.
- pop(): Removes and returns an arbitrary element from the set.
- clear(): Removes all elements from the set.
- copy(): Returns a shallow copy of the set.

These methods help in modifying or accessing elements efficiently without duplicates.

Note:
- Sets do not support indexing, slicing, or ordered operations.
- All elements in a set must be immutable (e.g., int, str, tuple). Mutable types like lists or dictionaries are not allowed.

Set Operations (covered next):
- union(), intersection(), difference(), symmetric_difference(), etc.

"""
