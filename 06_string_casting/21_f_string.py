# ********** f-string **********

name: str = "John"
age: int = 20
first_letter: str = name[0]
my_weight: float = 70.532000


# using f-strings
# Using Named Placeholders (Best for Readability)
my_string: str = f'My name is {name} and I am {age} years old.'
print("my_string: ", my_string)

# At the same time it could be f and r as well
my_string: str = fr'My \name is {name} and I am {age}\n \t years \old.'
print("my_string: ", my_string)
