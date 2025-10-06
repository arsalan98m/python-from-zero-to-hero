staff = [("Abid", 16), ("Noman", 17), ("Owais", 15)]

# Note: the else block is executed only if the loop is not terminated by a break statement

# this technique is used to search for a specific item in a list
for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff and hiring")
        break
else:
    print("No one is eligible to manage the staff and hiring")
