class TeaLeaf:
    def __init__(self, age):
        """
        _ this underscore doesn't mean on its own anything. It's just a python way of
        saying that hey this is an interesting property.  This shouldn't be allowed
        to touch directly. There needs to be a way of reading this property as well 
        as writing to this property. An this is a _ symbol which is used through out
        the industry. So whenever you see an _ underscore that means, this is having
        some thing special as a meaning. Now surely this can be done without underscore
        as weill. But this is such a common thing and Python also knows this so python
        doesn't treat this in a lot of places as _age you'll see `age` treated like this.
        """
        self._age = age

    # Responsible for reading the property
    @property
    def age(self):
        return self._age

    # Responsible for updating the property
    # After using decoration property, we can use the property name as a method
    # and we can use the setter decorator to update the property

    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea Leaf age must be between 1 and 5")


tea_leaf = TeaLeaf(2)
print(tea_leaf.age)

tea_leaf.age = 10
