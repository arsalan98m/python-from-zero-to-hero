"""
Accessing Base Class

In Order to understand this there are couple of ways where you actually do
something known as `Code Duplication` and we really want to avoid that.
There are couple of ways there is an explicit call and there is something
known as `super`, first of all there is `Code Duplication`, the second
one is known as `Explicit Call` and the third one is known as `super`.

So all of these methods are a way how you can access your base class if
you are trying to do the inheritance. And again there is no right or wrong
it all depends on the situation and there are usual trade offs. But most
of the time you're going to use the `super` method. because it's simpler
easier to understand and it's easier to maintain.   

Let's see the demo of this one 
"""


class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

# Example #1: Code Duplication


class GingerChaiCodeDuplication(Chai):
    def __init__(self, type_, strength, spice_level):
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level


# Example #2: Explicit Call
class GingerChaiExplicit(Chai):
    def __init__(self, type_, strength, spice_level):
        Chai.__init__(self, type_, strength)
        self.spice_level = spice_level

# Example #3: super()


class GingerChaiSuper(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level
