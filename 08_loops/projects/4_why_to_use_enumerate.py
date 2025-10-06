"""
You're creating a tea menu board.
Each item must be numbered.

Task:
- Use enumerate() to print menu items with numbers.
"""

menu = ["Green Tea", "Lemon Tea", "Spiced", "Mint"]

# for m in menu:
#     print(f"Menu item is {m}")

# for idx, item in enumerate(menu):
#     print(f"Menu item is {idx}, {item}")


for idx, item in enumerate(menu, start=1):
    print(f"Menu item is {idx}, {item}")
