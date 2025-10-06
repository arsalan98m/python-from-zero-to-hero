"""
Accessing List Elements

You can access elements using indexing (starting from 0) and negative indexing (starting from -1).

- Index starts from 0.
- You can use negative numbers to count from the end: -1 is last, -2 is second last.
"""

fruits: list = ["apple", "banana", "cherry"]

# Accessing list elements using positive indexing (starts from 0)
print("First fruit:", fruits[0])  # apple
print("Second fruit:", fruits[1])  # banana
print("Third fruit:", fruits[2])  # cherry

print("-" * 10)

print("Last fruit:", fruits[-1])  # cherry
print("Second last fruit:", fruits[-2])  # banana
print("Third last fruit:", fruits[-3])  # apple
