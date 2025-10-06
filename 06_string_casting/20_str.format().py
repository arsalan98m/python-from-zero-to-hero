# ********** str.format() **********

name: str = "John"
age: int = 20
first_letter: str = name[0]
my_weight: float = 70.532000

# ✅ Example 1: Basic usage (order matters)
my_string: str = "My name is {} and I am {} years old.".format(name, age)
print(my_string)

# ✅ Example 2: Using index numbers
my_string: str = 'My name is {1} and I am {0} years old.'.format(
    age, name)
print(my_string)
