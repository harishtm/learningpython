"""
    Program to demonstrate Sealed classes in python old style in python3.6
    Hint: Use metaclass
    
    stop classes from inherting/subclassing
    java final/.net sealed
    The current code implementation in python3.6 the same can be implemented in python2.x via meta classes
"""

class Final(type):

    def __new__(cls, name, bases, classdict):
        for b in bases:
            if isinstance(b, Final):
                raise TypeError("type '{0}' is not an acceptable base type".format(b.__name__))
        return type.__new__(cls, name, bases, dict(classdict))


class Foo(metaclass=Final):
    pass


class Bar(Foo):
    pass


