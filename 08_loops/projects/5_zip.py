"""
You're preparing an order summary with customer names
and their total bill.

Task:
- Use two lists: one for names and one for bills.
- Print: "[Name] paid $[amount]"
"""


names = ["Arsalan", "Bilal", "Noman", "Oman"]
bills = [50, 70, 100, 55]


for item in zip(bills, names):
    print(item)
    print(item[0])
    print(item[1])
