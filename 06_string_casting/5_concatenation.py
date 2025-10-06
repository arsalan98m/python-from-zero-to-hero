"""
String Concatenation in Python
------------------------------

String concatenation means **joining two or more strings** into a single string.

Python provides multiple ways to concatenate strings:

1. Using the `+` Operator
--------------------------
The most common method.

Example:
    first_name = "John"
    last_name = "Doe"
    full_name = first_name + " " + last_name
    print(full_name)  # Output: John Doe

2. Using `+=` Operator
-----------------------
Used to append to an existing string variable.

Example:
    message = "Hello"
    message += " World"
    print(message)  # Output: Hello World

3. Using `join()` Method
--------------------------
Efficient way to concatenate many strings, especially in loops.

Example:
    words = ["Python", "is", "fun"]
    sentence = " ".join(words)
    print(sentence)  # Output: Python is fun

4. Using f-Strings (Python 3.6+)
--------------------------------
Modern and readable way of combining strings and variables.

Example:
    name = "Alice"
    age = 30
    print(f"My name is {name} and I'm {age} years old.")
    # Output: My name is Alice and I'm 30 years old.

5. Using `format()` Method
---------------------------
Older alternative to f-strings.

Example:
    language = "Python"
    print("I love {}".format(language))  # Output: I love Python

Notes:
------
- Concatenation only works between **strings**. You must convert numbers or other types to string first.

Example:
    age = 25
    print("Age: " + str(age))  # Correct
    # print("Age: " + age)     # ❌ TypeError

"""

# ✅ 1. Using + Operator
first_name: str = "John"
last_name: str = "Doe"
full_name: str = first_name + " " + last_name
print("Full Name:", full_name)

# ✅ 2. Using += Operator
greeting: str = "Hello"
greeting += " World"
greeting += "!"
print("Greeting:", greeting)

# ✅ 3. Using "".join() Method
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print("Sentence:", sentence)

# ✅ 4. Using f-Strings (recommended for modern Python)
name = "Alice"
age = 30
print(f"My name is {name} and I'm {age} years old.")

# ✅ 5. Using format() Method
language = "Python"
version = 3.12
print("I code in {} version {}".format(language, version))

# ✅ 6. Concatenation with Numbers (must convert to string)
score = 100
# print("Your score is " + score)  # ❌ TypeError
print("Your score is " + str(score))  # ✅ Correct
