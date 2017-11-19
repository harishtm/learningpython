"""
	You can use wraps as a decorator to fix docstrings and names of decorated functions.
	Why does this matter? This sounds like a weird edge case at first, but if you are
	writing an API or any code that someone other than yourself will be using, then
	this could be important. The reason being that when you use Pythons introspection
	to figure out someone else code, a decorated function will return the
	wrong information
"""

from functools import wraps


def without_wraps(func):
	def __wrapper(*args, **kwargs):
		return func(*args, **kwargs)
	return __wrapper


def with_wraps(func):
	@wraps(func)
	def __wrapper(*args, **kwargs):
		return func(*args, **kwargs)
	return __wrapper


@without_wraps
def myfunc_a():
	""" I am in function A without wraps """
	pass


@with_wraps
def myfunc_b():
	""" I am in function B with wraps """
	pass


if __name__ == "__main__":
	print "Doc String : ", myfunc_a.__doc__, " Function Name : ", myfunc_a.__name__
	print "Doc String : ", myfunc_b.__doc__, " Function Name : ", myfunc_b.__name__
