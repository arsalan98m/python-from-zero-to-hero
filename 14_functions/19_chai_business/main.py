# 📌 One way to import
# import recipes.flavors


# print(recipes.flavors.elachai_chai())
# print(recipes.flavors.ginger_chai())


# 📌 Another way to import
# from recipes.flavors import elachai_chai, ginger_chai


# print(elachai_chai())
# print(ginger_chai())

# 📌 Another way to import ❌ (Avoid this)
# from .recipes.flavors import ginger_chai

# ❌ (Avoid this)
# from masala_chai import *


# Note: __init__.py turns folder into a python package and don't write anything in it. It can contain initialization code but it's ok
