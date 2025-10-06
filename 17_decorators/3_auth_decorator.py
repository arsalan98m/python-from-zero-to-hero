from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
            return None
        else:
            func(user_role)
    return wrapper


@require_admin
def access_tea_inventory(role):
    print(f"Accessing tea inventory as {role}")


access_tea_inventory("user")
access_tea_inventory("admin")
