"""
The decorators are simply a way of decorations. Now they could be functional as well but
the primary agenda is decoration. Decoration is something that you do on top of something.
For example, when you buy coffee, some people actually sprinkles a little bit of a chocolate
powder or coffee on top of it that's decoration of coffee. Now sometimes it changes the taste
a little but, sometimes it doesn't. Sometimes it add more value to it. Sometimes it's just
a wrapper around it. This is the whole point of having the decorator. It is just a wrapper
around your function and python gives you actually some superpower.

Write a decorator that measures the time time a function takes to execute.
"""

from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    """
     Here returning wrapper will change the metadata about the greet function.
     To avoid this, we can use the wraps decorator from functools.
    """
    return wrapper


@my_decorator
def greet():
    print("Hello from decorators class")


greet()

"""
Now if i want to print the greet.__name__ it will return the wrapper function name.
Why wrapper? Our function name was greet because technically what we are returning
back is actually a wrapper so this is a common syntax and common thing which is
done that hey the name of function and couple of other metadata about the function
changes. To avoid this we can use the wraps decorator from functools. The whole
job of this wraps is to make sure to preserve the metadata about the function.
"""
print(greet.__name__)
