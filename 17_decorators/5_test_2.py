def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")

        result = func()
        return result
    return wrapper


@log
def greet():
    print("Hello!")
    return 10


print(greet())
