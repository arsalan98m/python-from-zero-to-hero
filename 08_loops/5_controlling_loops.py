"""
Controlling Loops
Python provides two keywords (break & continue) to control loops:

- break: Exits the loop immediately.
-continue: Skips the rest of the code in the current iteration and moves to the 
next iteration.
"""

# Break example
print("----------Break example-------------")
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# Continue example
print("----------Continue example-------------")
for i in range(5):
    if i == 3:
        continue
    print(i)  # Prints 0, 1, 2, 4
