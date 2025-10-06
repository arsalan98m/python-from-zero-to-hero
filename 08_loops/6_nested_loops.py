"""
Nested Loops

What are nested loops?

Nested loops, also known as inner loops or nested iterations, refer to the 
process of placing one loop inside another loop. The inner loop will iterate 
through its entire cycle for each iteration of the outer loop.

"""

# Multiplication table
for outer in range(1, 6):  # outer loop
    print(f"Multiplication table for {outer}:")
    for inner in range(1, 6):  # nested inner loop
        print(f"{outer} * {inner} = {outer * inner}")
    print()  # Add a blank line after each row
