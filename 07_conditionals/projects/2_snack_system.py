snack_input = input("Enter a snack:").lower()


if snack_input == "cookie" or snack_input == "samosa":
    print("Order is confirmed")
else:
    print(f"{snack_input} is unavailable")
