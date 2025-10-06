"""
Attribute Shadowing

What is attribute shadowing?

The term sounds really fancy but the implementation is super easy. 
The concept is easy but it has its own meaning. 

inside the Class Chai, is_hot is an attribute or a variable
When we actually go head and have this is_hot inside a class
then this whole thing variable is called as attribute. 

We got the first part attribute.

But what is shadowing?
If somehow the reference of the variable `temperature` or object attribute 
is no longer available then it fallbacks to the value of the attribute which
was defined in the `Chai` itself. We can see this in line no 38.

In line no 34 we can see we injected that cup attribute, but we actually
deleted that attribute in line 40. So there is no fallback but if it happens
that the fallback is there in the Chai class it will get the value, the default
fallback there and that's exactly the shadowing. So if there is nothing to
fallback the shadow will fall onto the class itself. If it doesn't exist in
the class, there is no fallback for it. That is your attribute shadowing.

"""


class Chai:
    temperature = "hot"
    strength = "Strong"


cutting_chai = Chai()
print(f"Cutting Chai: {cutting_chai.temperature}")

cutting_chai.temperature = "Mild"
cutting_chai.cup = "small"
print(f"After Updating Cutting Chai: {cutting_chai.temperature}")
print(f"Direct look into the class : {Chai.temperature}")

del cutting_chai.temperature
del cutting_chai.cup
print(
    f"After Deleting temperature in Cutting Chai: {cutting_chai.temperature}")

# ❌ AttributeError: 'Chai' object has no attribute 'cup'
# print(
#     f"After Deleting cup in Cutting Chai: {cutting_chai.cup}")
