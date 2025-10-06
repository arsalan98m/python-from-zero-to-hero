class ChaiOrder:
    def __init__(self, type_, size):
        print("Initializing a new chai order")
        """
        Now you might be wondering whats' the type_ why we given an
        extra underscore to this type? Does without underscore work?
        Yes but you see an extra formatting. Why this extra formatting?
        Because actually type is an operator in python. It's a function
        which gives me the type of whatever you ask it. It is supposed
        to use with the function, but since on our case it make sense
        to use the type, that's why i used the type but i actually 
        added an underscore to it. This is a common practice in production
        as well.

        Every class has a constructor. If you don't create a constructor,
        the class will automatically create one behind the scene at the 
        time of execution.
        """
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size} of {self.type} chai"


order = ChaiOrder("Masala", "Large")
print(order.summary())
