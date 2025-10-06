# Nested if Statements
# if statements can be nested inside other if statements to check multiple conditions.

num: int = 10
# num: int = -10

if num > 0:  # check weather the number is positive or negative

    if num % 2 == 0:  # Modulus operator, remainder 0 = even_number,
        print("The number is positive and even.")
    else:  # remainder 1 = odd_number,
        print("The number is positive and odd.")

else:
    print("The number is negative.")
