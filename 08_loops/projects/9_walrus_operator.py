"""
Walrus operator

:=

x = 5 => This is a statement, it assigns a value to a variable

3 + 3 => This is an expression because it returns a value


"""

# Without walrus operator

# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

# With walrus operator
value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")


available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter you chai cup size:")) in available_sizes:
    print(f"We have {requested_size} size available")
else:
    print(f"We don't have {requested_size} size available")
