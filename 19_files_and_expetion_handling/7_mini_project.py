class InvalidChaiError(Exception):
    pass


def bill(flavour, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavour not in menu:
            raise InvalidChaiError("that chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavour] * cups
        print(f"Your bill for {cups} cups of {flavour} chai: rupees {total}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for visiting our chai shop")


bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)
