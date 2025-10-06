"""
Object Oriented Programming

Now this Object Oriented Programming or in short known as OOP is also termed as OOPs,
There is no exact shortcut or a long cut of this one, it's sometime called as 
Object Oriented Programming systems. That's why the name OOPs here. But again the concepts
are pretty simple and easy. Now one thing you always have to remember that this object
oriented programming is a paradigm of programming. What do i mean by paradigm?
Paradigm simply stands for it's a way of writing the code. Now this way of writing the
code got evolved during the C++ era and after that a lot of programming languages 
adopted it. Java, JavaScript, Kotlin, Swift etc. Now this is nothing new a whole lot of
applications are being written with this kind of a style of writing programming. But 
there are lots of other ways of writing programming syntaxes and programming softwares
as in general. One of them is functional programming and these days functional programming
is much more preferred compared to the classic object oriented. And in majority of the
software that you'll see in the production there is always a mix of little bit functional,
little bit of Object Oriented Programming. There is no right, there is no wrong but yes
through the object oriented programming we learn a little bit about new data structures 
and we learn how to engage with them. As well as we also learn about the some the new
terminologies which are pretty common things like polymorphism, abstraction although they
are very in general english terms and they mean exactly same as what they mean in general
as they mean in the programming paradigm as well.

Important Note:
Always remember everything in python is an object.
So although type(Chai) says i'm a class but in reality
this class `Chai` is also an object.

"""

# Creating class


class Chai:
    pass


class ChaiTime:
    pass


print(type(Chai))  # <class 'type'>

# Creating an object
ginger_tea = Chai()
print("type(ginger_tea) = ", type(ginger_tea))
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)
