# i can mutate this
spice_mix = set()

print(f"Initial spice mix id: {id(spice_mix)}")

spice_mix.add("Ginger")
spice_mix.add("Cardamom")

print(f"After Update spice mix id: {id(spice_mix)}")
print(spice_mix)
