seat_type = input("Enter the seat type (sleeper, AC, general, luxury)").lower()


match seat_type:
    case "sleeper":
        print("Sleeper - No AC, Beds available")
    case "AC":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - No AC, Seats available")
    case "luxury":
        print("Luxury - Air conditioned, comfy ride")
    case _:
        print("Invalid seat type")
