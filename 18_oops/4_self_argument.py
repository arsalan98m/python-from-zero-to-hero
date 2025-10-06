"""
self argument

So far we have been seen that we are just creating properties.
Now we want to see how we can create methods, methods are just 
a fancy name to functions if they are created inside the class,
they are called as methods.

The first thing that you always do in all the methods is you write
`self` as the first argument. This is the step 1. What is this self
that we are passing in the method? `self` is a reference to all the
properties that we define in the class, just after passing this `self`
inside method we can actually refer to any variable that we have defined
within the class.
"""


class Chaicup:
    size = 150  # ml (milliliter)

    def describe(self):
        return f"A {self.size}ml cup chai"


cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))
