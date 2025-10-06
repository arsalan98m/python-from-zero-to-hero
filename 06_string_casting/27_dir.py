# # prompt: print list of str functions using dir(), dont show function starting with"__"

# Get the list of string methods
string_methods: str = dir(str)

# # Filter out methods starting with "__"
filtered_methods: str = [
    method for method in string_methods if not method.startswith("__")]

# Print the filtered list
filtered_methods
print(filtered_methods)
