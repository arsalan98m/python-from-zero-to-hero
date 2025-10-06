def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai...")
        if flavour == "unknown":
            raise ValueError("We don't know that flavour")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Chai is ready")
    finally:
        print("Thank you for visiting our chai shop")


serve_chai("unknown")
