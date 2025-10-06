"""
for Loop with else in Python

In Python, a for loop can have an else block. The else block runs only if the loop completes without a break 
statement.
"""

# Example 1: for loop with else (No break)
print("----------Example 1: for loop with else (No break)-------------")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
else:
    print("Loop completed successfully")


# Example 2: for loop with break (Skipping else)
print("----------Example 2: for loop with break (Skipping else)-------------")
for num in numbers:
    print(num)
    if num == 3:
        print("Breaking the loop.....")
        break
else:
    print("Loop completed successfully")


# Example 3: for loop with continue (Skipping else)
print("----------Example 3: for loop with continue (Skipping else)-------------")
for num in numbers:
    print(num)
    if num == 3:
        print("Skipping 3.....")
        continue

else:
    print("Loop completed successfully")


# Example 4: Searching with else
print("----------Example 4: Searching with else-------------")
for num in numbers:
    if num == 6:
        print("Number found!")
        break
else:
    print("Number not found!")  # Runs because 6 is not in the list
