def chai_customer():
    print("Welcome! What chai would you like?")

    order = yield
    while True:
        print(f"Preparing your {order}...")
        order = yield


stall = chai_customer()
next(stall)  # start the generator

stall.send("Masala chai")
stall.send("Lemon chai")

"""
▶️ next(stall)
➡️ Prints welcome message
➡️ Pauses and waits

▶️ stall.send("Masala chai")
➡️ Prints "Preparing your Masala chai..."
➡️ Pauses and waits again

▶️ stall.send("Lemon chai")
➡️ Prints "Preparing your Lemon chai..."
➡️ Pauses again

And this continues...

"""
