# The elif Statement
# The elif statement is used to check multiple conditions. It stands for "else if."


num: int = 0

if num > 0:  # Program execution step# 1 if condition = False
    print("The number is positive.")
elif num < 0:  # Program execution step# 2 if condition = False
    print("The number is negative.")
else:  # Program execution step# 3 python will execute the else block
    print("The number is zero.")
