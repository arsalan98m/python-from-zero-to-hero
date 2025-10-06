chai_menu = {
    "masala": 30,
    "ginger": 30,

}

try:
    chai_menu["elaichi"]
except KeyError:
    print("Elaichi is not in the menu")


print("Hello chai")
