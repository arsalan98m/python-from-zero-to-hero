# Print numbers from 0 to 4
for i in range(5):
    print(i)

print("\n--------------------------------\n")

# Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)

print("\n--------------------------------\n")

for _ in range(10):  # Just to show that _ is a loop variable, but its throwaway variable
    # Code to be executed 100,000 times
    print(f"Hello, World! Iteration {_}")
