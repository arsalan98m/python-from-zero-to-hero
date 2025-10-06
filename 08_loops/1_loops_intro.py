"""
Tutorial: Loops and Iteration in Python
=======================================

1. Introduction to Loops
--------------------------
Loops are used to execute a block of code multiple times. Python supports two primary loop structures:

- for loops: Iterate over a sequence like a list, string, or range.
- while loops: Execute a block of code repeatedly as long as a condition is True.

2. When to Use Which Loop
--------------------------

A. For Loop
------------
The for loop iterates over a sequence (like a list, string, or range) and executes a block of code for each item for a 
specified or fixed number of times.

Best used when the number of iterations is known or finite, such as when iterating over elements in a list.

Example Scenarios:
- Grading a class of students: Iterate over a list of students to compute scores.
- Devices like washing machines or microwave ovens with a fixed number of cycles.

B. While Loop
--------------
Ideal when the number of iterations is unknown and depends on a condition that becomes False over time.

Example Scenarios:
- Filling up a gas tank until full.
- Home appliances like air conditioners, refrigerators, heaters, or washing machines during the water fill phase, which continue running based on sensor conditions.

Loops allow for efficient automation and repetitive task handling in programming.
"""

# Example 1: For Loop

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
# Note: Membership Operators in Python in, not in
for fruit in fruits:
    print(fruit)


# Iterate over a string
word: str = "Python"
for letter in word:
    print(letter)
