
"""
*args is used to pass a variable number of arguments to a function.
**kwargs is used to pass a variable number of keyword arguments to a function.
"""


def special_chai(*ingredients, **extras):
    print("Ingredients: ", ingredients)
    print("Extras: ", extras)


special_chai("Cinnamon", "Cardamon", sweetener="Honer", milk="Yes")
