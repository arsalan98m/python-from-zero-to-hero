"""
staticmethod vs classmethod

In the last lecture, we saw how the `staticmethod` works. And it is a pretty way to declare 
Utilities and all those things. But there is one drawback or kind of a thing where the
`staticmethod` doesn't work really well, which is when you initialize an object, the
`staticmethod's` are never designed to initialize any objects, it just work is designed to
so that class can actually direct invoke that and can just use it like a utility. But there
is also one more interesting thing which is how do you control the constructor? We have
seen we can use init method for declaring a constructor, but can we have more than one
constructor? Sadly, no. You can have just one constructor, but there are ways to control the
constructor and get a feeling like we have more than one constructor and more than one
ways of kind of initiating an object from the class itself, it's a very interesting topic
and sometimes it feels like it's very similar to the `staticmethod` but it's not.

 
Class Methods Comparison
------------------------
+------------------+-----------------------------------+-------------------------------------+
| Feature | @classmethod | @staticmethod |
+------------------+-----------------------------------+-------------------------------------+
| First parameter | Receives `cls` (the class itself) | Receives no automatic first argument|
+------------------+-----------------------------------+-------------------------------------+
| Use case         | Operate on the class, not instance | Utility function related to class   |
+------------------+-----------------------------------+-------------------------------------+
| Access to `cls` | Yes | No |
+------------------+-----------------------------------+-------------------------------------+
| Access to `self` | No | No |
+------------------+-----------------------------------+-------------------------------------+
 
Example:
There could be a chance that somebody might provide you a value in dictionary format or
may be a string format and you want to have a constructor just like we have created in
below. Then whenever an object is being created, somebody can provide me direct values.
we accept that, somebody can provide me the value in dictionary format we accept that.
And somebody can provide me the value in string format we accept that. That is the whole
goal.

"""


class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        """
        This is almost internally, like calling the constructor from the same class.
        The cls is a reference to the class. So when i just say cls() so i'm just 
        passing the whole values with in the __init__ constructor behind the scenes.
        """
        return cls(order_data['tea_type'], order_data['sweetness'], order_data['size'])

    @classmethod
    def from_str(cls, order_string):
        tea_type, sweetness, size = order_string.split(',')
        return cls(tea_type, sweetness, size)


order_1 = ChaiOrder.from_dict(
    {'tea_type': 'Masala', 'sweetness': '50%', 'size': 'Large'})
print(order_1.__dict__)

order_2 = ChaiOrder.from_str('Green, 100%, Medium')
print(order_2.__dict__)


class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ['Small', 'Medium', 'Large']
