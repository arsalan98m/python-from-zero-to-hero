my_string: str = "Hello, World! Hello, Pakistan"

starting_index = my_string.find("Hello")
print("starting_index = ", starting_index)  # Output: 0

starting_index2: str = starting_index + len("Hello")  # 0 + 5 => 5
print("starting_index2 = ", starting_index2)  # Output: 5

# after replacing ", World! Hello, Pakistan"
print(my_string[starting_index2:])  # Output: , World! Hello, Pakistan
print(my_string[starting_index2:].find("Hello"))  # Output: 9
