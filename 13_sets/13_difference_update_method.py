# Use difference_update() method to remove multiple element at once.

my_set: set = {1, 2, 3, 4, 5, 'A', 'a'}
print("Before: my_set = ", my_set)  # {1, 2, 3, 4, 5, 'A', 'a'}
my_set.difference_update({1, 5, 3, 'A'})
print("After:  my_set = ", my_set)  # {2, 4. 'a'}
