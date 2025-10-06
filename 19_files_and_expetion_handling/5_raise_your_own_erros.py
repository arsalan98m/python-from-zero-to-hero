def brew_chai(flavour):
    if flavour not in ["masala", "ginger"]:
        raise ValueError("We don't know that flavour")
    print(f"Brewing {flavour} chai...")


brew_chai("unknown")
