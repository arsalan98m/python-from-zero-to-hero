"""
Some chai flavours are out of stock.
You want to skip those and stop entirely if someone requests a restricted flavour.

Task:
- Skip if flavor is `Out of Stock`.
- Break if flavour is `Discontinued`.

"""

flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} item found")

print(f"{flavour} Outside of loop")
