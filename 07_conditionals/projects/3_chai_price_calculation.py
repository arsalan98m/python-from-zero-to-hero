user_input = input("Enter a cup size: ").lower()

if user_input == "small":
    print("Price is Rs.10")
elif user_input == "medium":
    print("Price is Rs.15")
elif user_input == "large":
    print("Price is Rs.20")
else:
    print("Unknown cup size")
