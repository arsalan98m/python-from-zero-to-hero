

def add_stars(func):
    def wrapper(*args, **kwargs):
        print("**********")
        func(*args, **kwargs)
        print("**********")
    return wrapper

# Without decorator
# def say_hello():
#     print("Hello!")


# wrapped_say_hello = add_stars(say_hello)
# wrapped_say_hello()

# With decorator
@add_stars
def say_hello(name, age):
    print(f"Hello {name}! {age}")


say_hello("John", 20)
