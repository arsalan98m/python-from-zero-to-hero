user = {"username": "arsalan"}
user.setdefault("role", "admin")
print(user)
# Output: {'username': 'arsalan', 'role': 'admin'}

# If key already exists, value won't be changed
user.setdefault("role", "guest")
print(user)
# Output: {'username': 'arsalan', 'role': 'admin'}
