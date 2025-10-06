
"""
The walrus operator in Python is written as :=. It's a way to assign a value to a variable as part of an expression.

The walrus operator is just a shortcut to assign and use a value in one go, 
useful in loops or conditions to write cleaner, shorter code.

It's a new feature in Python 3.8.

Let's break it down into baby steps:
"""

# 🐣 Step 1: Normally, you do assignments like this:
# You first assign x = 10, then check it in an if.
x = 10
if x > 5:
    print("x is greater than 5")


# 🐥 Step 2: Walrus operator does both at once:
if (x := 10) > 5:
    print("x is greater than 5")

"""
Here:
- x := 10 assigns 10 to x
- Then checks if x > 5
- If true, it prints x

✅ So it assigns and checks in one line.
"""

# 🐤 Step 3: Why is this useful?
# Imagine you’re repeating a function call:

# Without walrus
value = input("Enter: ")
while value != "q":
    print(f"You typed {value}")
    value = input("Enter: ")

# Using the walrus operator:
# With walrus (💡 It saves a line and avoids repeating input()).
while (value := input("Enter: ")) != "q":
    print(f"You typed {value}")

# 🐓 Step 4: Syntax rule
# You must wrap the walrus expression in parentheses when used inside conditions or loops:

# ✅ Correct
while (n := input()) != "stop":
    print(n)

# ❌ Error if you skip ()
while n := input():  # SyntaxError
    print(n)
