"""
When you use a decorator, you're replacing one function with another.
"""

from functools import wraps

def logged(func):
	def with_logging(*args, **kwargs):
		return func(*args, **kwargs)
	return with_logging


def f(x):
	""" does some math """
	return x + x * x


g = logged(f)


def wraplogged(func):
	@wraps(func)
	def with_logging(*args, **kwargs):
		return func(*args, **kwargs)
	return with_logging
	

h = wraplogged(f)

if __name__ == "__main__":
	
	print f.__doc__, f.__name__
	print g.__doc__, g.__name__ 
	print h.__doc__, h.__name__ 



