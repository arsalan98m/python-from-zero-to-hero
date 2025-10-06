# old way

# file = open("order.txt", "w")
# try:
#     file.write("masala chai")
# except Exception as e:
#     print(f"Error: {e}")
# finally:
#     file.close()


# new and modern way (It happens everything safely)

with open("order.txt", "w") as file:
    file.write("ginger chai")
