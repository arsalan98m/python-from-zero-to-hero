"""
What are Generators comprehension?

Generators are a type of iterable in python that can be used to create a sequence of values.
They are similar to lists but they are more efficient because they don't store all the values in memory.
They generate values on the fly.

[x for x items] # make entire list in memory

(x for x in items) # like a stream (all of your memory not clogged at once)

"""

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)
