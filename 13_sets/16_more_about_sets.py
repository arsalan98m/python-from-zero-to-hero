
my_set:  set = {1, 2, 3, "Hello! World", 4, 5, 6}
my_set2: set = {1, 2, 3, "Hello! World", 8, 9}
my_set3: set = {1, 2, 3, "Hello! World", 77}

"""
💡 What difference() Means:
Returns a set with elements that are only in my_set, but not in my_set2 or my_set3.
"""
print("difference()           = ", my_set.difference(my_set2, my_set3))


"""
💡 What intersection() Means:
Returns a set with elements that are common to all sets.
"""
print("intersection()         = ", my_set.intersection(my_set2, my_set3))


"""
💡 What union() Means:
Combines all unique elements from all sets into one set.
"""
print("union()                = ", my_set.union(my_set2, my_set3))

"""
💡 What symmetric_difference() Means:
Returns elements that are in either one set or the other, but not both.
"""
print("symmetric_difference() = ", my_set.symmetric_difference(my_set2))

"""
💡 What isdisjoint() Means:
Returns True if no elements are common between the sets.
"""
print("isdisjoint()           = ", my_set.isdisjoint(my_set2))

my_set2 = {1, 2, 3, "Hello! World"}
"""
💡 What issubset() Means:
- Is the small box (my_set2) completely inside the big box (my_set)?
- ✅ Yes, because all elements of my_set2 exist in my_set.


💡 What issuperset() Means:
- Is the big box (my_set) completely covering the small box (my_set2)?
- ✅ Yes, because my_set contains everything my_set2 has (and more).


"""
print("issuperset()           = ", my_set.issuperset(my_set2))

print("issubset()             = ", my_set2.issubset(my_set))
