#!/usr/bin/python3
# 0-add_integer.py
# Bernard B. Sakyi
"""Defines an integer addition function."""


def add_integer(a, b=98):
	"""Returns an integer: the addition of a and b.
	
	Float varguments are typecasted ton int before the addition is performed.
	
	Raises:
		TypeError: If either a or b is a non-integer and non-float.
	"""
	if ((not isinstance(a, int) and not isinstance(a, float))):
		raise TypeError("a must be an integer")
	if ((not isinstance(b, int) and not isinstance(b, float))):
		raise TypeError("b must be intger")
	return (int(a) + int(b))	
