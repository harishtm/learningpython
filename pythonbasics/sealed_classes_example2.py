"""
    Program to demonstrate Sealed classes in python3.x style
    Using: __init_subclass__
"""

class Base:

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls is not Base:
            # raise TypeError("type '{0}' is not an acceptable base type".format(cls.__name__))
            raise TypeError("Base does not support polymorphism. Use composition over inheritance.")


class Derived(Base):
    pass
