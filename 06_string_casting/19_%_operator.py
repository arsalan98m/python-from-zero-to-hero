
name: str = "John"
age: int = 20
first_letter: str = name[0]
my_weight: float = 70.532000


print(type((name, first_letter, age, my_weight)))

# using % operator
my_string: str = '''My names is %s, first letter of my name is \%c\, I am %d years old and my weight is %f kg''' % (
    name, first_letter, age, my_weight)
print(my_string)

my_string = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %.2f Kg.''' % (
    name, first_letter, age, my_weight)  # Dont forget period %.2f
print(my_string)

# String Formatting in Python – Does Order Matter?
# Yes, order matters when using string formatting in Python, especially with the % operator, .format(), and f-strings (f""). Let's break it down:
my_string: str = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %f Kg.''' % (
    my_weight, age, name, first_letter)
