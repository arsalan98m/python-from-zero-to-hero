"""
So we have talked recently about inheritance and now we want to talk about
multiple inheritance. Now to be honest there is nothing too much to talk
about for multiple inheritance. You can have comma separated as many classes
as you want to have in that. Usually we don't prefer to have too many classes
two are more than enough for us but even having two of these classes as inherited
classes it sometimes can create problems. We will walk through an example of
this. But the topic that we want to discuss in this is pretty interesting. If
you look at this, this is known as method resolution order.

What is method resolution order?

If we look at the documentation this is what it says at the very top of the
documentation. It was introduced in Python 2.3 but it is still used including
in the Python 3
"""


class A:
    label = "A: Base class"


class B(A):
    label = "B: Masala blend"


class C(A):
    label = "C: Herbal blend"


"""
Inside the print we get the "B: Masala blend" why? because whichever the class first
inside multiple inheritance, if there is any common such method which are being called
up, it is being called from the very first class that you are inheriting.
"""


class D(B, C):
    pass


cup = D()
print(cup.label)

# This will print hierarchy
print(D.__mro__)
