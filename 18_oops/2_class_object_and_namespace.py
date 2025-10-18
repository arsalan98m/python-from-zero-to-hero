"""
Each object has it own entity that is called namespace. It can
posses its own features and methods or properties but doesn't
bother other ones, This is exactly the namespaces and the 
concept of namespaces in the world of object oriented programming.

Important Note:
Each object is actually having it's own namespace which doesn't
effect other objects also doesn't effect the classes as well by default
If you wish you can but by default it does not change any value.
 
"""


class Chai:
    # This is a property
    origin = "Pakistan"


print("Chai.origin = ", Chai.origin)  # Output: Pakistan

# Adding more properties
Chai.is_hot = True
print("Chai.is_hot = ", Chai.is_hot)  # Output: True

# Creating objects from class Chai
masala = Chai()
print("masalan.origin = ", masala.origin)  # Output: Pakistan
print("masalan.is_hot = ", masala.is_hot)  # Output: True

# Updating Property value
# If i change or update anything inside an object this change will not be propagated/update inside the class
# That's mean each object has it's own namespace which does not effect other objects also does not effect the classes as well by default.
# If you wish you can but by default it does not change any value.
masala.is_hot = False
print("After update masalan.is_hot = ", masala.is_hot)  # Output: False
print("After update Chai.is_hot = ", Chai.is_hot)  # Output: True

masala.flavour = "Masala"
print("masalan.flavour = ", masala.flavour)  # Output: Masala
print("Chai.flavour = ", Chai.flavour)  # AttributeError
