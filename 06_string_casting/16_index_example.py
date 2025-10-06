
my_string: str = "Hello, World! Hello, Pakistan"

print(my_string)  # Output: Hello, World! Hello, Pakistan
print(len(my_string))  # Output: 29

print('\n-----\n')

print("Substring to search    = ", "Hello")
print("Starting index         = ", len("Hello"))  # 5
print("End index              = ", len(my_string))  # 29

# index(substr, start, end)
print("Second Occurance index = ", my_string.index(
    "Hello", len("Hello"), len(my_string)))

# Uncomment to see ValueError: substring not found
# print("Second Occurrence index = ", my_string.index(
#     ("Hello7"), len("Hello"), len(my_string)))

print(my_string.find("Hello7"))  # -1 for not found
