# ********** List, Tuple & Set Conversions **********

# Python allows converting between lists, tuples, and sets.


# ✅ Example 1: Tuple → List

tup: tuple = (1, 2.7, 3, 'OB')
lst = list(tup)
print(lst, type(lst))

# ✅ Example 2: List → Set (Removes Duplicates)

lst: list = [1, 2, 2, 3, 4, 4, 5, "Agentic AI"]
s = set(lst)
print(s, type(s))
