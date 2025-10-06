"""
Intersection: Returns elements that are present in both sets
"""

my_set: set = {1, 2, 3, 5}
my_set_2: set = {1, 5, 6, 7}

# common_spices = my_set.intersection(my_set_2)
common_elements: set = my_set & my_set_2
print(f"Common elements are: {common_elements}")  # {1, 5}
