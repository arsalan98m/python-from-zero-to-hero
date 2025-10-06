def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


my_bill = calculate_bill(3, 15)
print(my_bill)

print("Order for table 2: ", calculate_bill(2, 10))

print("Order for table 3: ", calculate_bill(3, 15))

print("Order for table 4: ", calculate_bill(4, 20))

print("Order for table 5: ", calculate_bill(5, 25))
