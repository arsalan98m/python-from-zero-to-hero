"""
Inheritance

Just like you might have seen in the real life,, that some people inherit a
car, some people inherit some great amount of money, some people inherit some
house or a great property. That's exactly like how it works. If your dad has 
earned a great amount of property, you inherit that you don't start from
scratch. That's reality of life as well. So same we can do with the programming
as well. If some class has done some work, you can just go ahead and inherit 
that. Yeah that's allowed in programming. You can inherit from any class. Like
there are rules as well. But as of now let's see that we can inherit from any
class.

Let's see the demo of this one 
"""


class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")


class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


class ChaiShop:
    """
    If you are actually inheriting all the values of this BaseChai class,
    then you don't actually put the parenthesis inside the class. That's 
    the Syntax of Composition. When you actually create an object that's
    a whole different story.

    Sometimes we dont' want to inherit the classes, but we want to take a
    reference of it. So we have got the reference of it.
    """
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop.")
        self.chai.prepare()


class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve()
fancy.serve()
