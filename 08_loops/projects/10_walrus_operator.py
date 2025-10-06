flavours = ["masala", "ginger", "lemon", "mint"]

print("Available flavours: ", flavours)

while (flavour := input("Choose your flavour: ")) not in flavours:
    print(f"Sorry, {flavour} is not available")

print(f"You choose {flavour} chai!")
