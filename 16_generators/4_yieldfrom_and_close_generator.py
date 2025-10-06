
"""
In this portion of the Python Learning we are going to work on that we can actually
`yield` some value, in case we remember from the last lecture we are talking about 
the generators, we've seen quite a lot, quite a hidden details about them but now we
want to see two more things and that is it, that is all about the generators.

The one thing which is common is that sometimes generator doesn't generate the value 
or yield the value on it's own, it sometimes borrows the value from somewhere else.
That is totally possible, we are going to see a right example for that as well as 
sometimes you don't want to generate rest of the values from a generator or maybe
it's an infinite generator, we don't wanted to keep in the memory forever we want to 
close it down so that it's removed from the memory and we get the job done. This is 
a common scenario in the database whenever a function calls you yield a connection string
from the database and once it's all done you finally try to close this up. Although
the logic is bit different there in the database but you will see some how similar kind
of a example appear

`yield from`
`close()`
"""

# yield from
# def local_chai():
#     yield "Masala chai"
#     yield "Lemon chai"
#     yield "Ginger chai"


# def imported_chai():
#     yield "Matcha"
#     yield "Oolong"


# def full_menu():
#     yield from local_chai()
#     yield from imported_chai()


# for chai in full_menu():
#     print(chai)


# close()
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order..."
    except:
        print("Stall closed, No more chai!")


stall = chai_stall()
print(next(stall))


# This is the way to close the generator (this is actually a cleanup you are cleaning up the memory)
# generator stops automatically as well but we really want to gracefully stops the generator so
# there are no memory leaks, your program performs well, no memory crashes, tons of advantages.
stall.close()
