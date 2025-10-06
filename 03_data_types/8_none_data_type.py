"""
None Data Type in Python
In Python, None is a special data type that represents the absence of a value or a null object reference. 
It is a singleton object, meaning that there is only one instance of None in the entire Python environment.

- No value: None represents the absence of a value or a null object reference.

"""

x: str = None
y: str = None
z: str = x

print(type(x), "x = ", x)  # <class 'NoneType'> x =  None
print("value of x = ", str(x))  # value of x =  None
print("x == y =", x == y)  # x == y = True
print("id(x) = ", id(x))  # id(x) =  140733600000000
print("id(y) = ", id(y))  # id(y) =  140733600000000
print("id(z) = ", id(z))  # id(z) =  140733600000000
print("x is y = ", x is y)  # x is y = True
print("x is z = ", x is z)  # x is z = True
print("id(x) is id(z) = ", id(x) is id(z))  # id(x) is id(z) = False
print("id(x) == id(z) = ", id(x) == id(z))  # id(x) == id(z) = True

'''
In Python, `==` is the equality operator, which checks if the values of two objects are equal.

On the other hand, `is` is the identity operator, which checks if two objects are the same object in memory.
'''
print("*" * 20)

print("None is None = ", None is None)  # None is None = True
print("None == None = ", None == None)  # None == None = True
print("None == x = ", None == x)  # None == x = True
print("None is x = ", None is x)  # None is x = True
print("id(None) is id(None) = ", id(None)
      is id(None))  # id(None) is id(None) = False
