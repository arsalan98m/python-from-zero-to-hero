"""
Syntax of list comprehension

[expression for item in iterable if condition]

"""

menu = [
    "Masala chai",
    "Iced Leamon tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)
