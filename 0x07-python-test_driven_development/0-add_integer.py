#!/usr/bin/python3
""" this is a module of addition of numbers
"""
def add_integer(a, b=98):
    """ a function which add two number
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int)):
        raise TypeError("b must be an integer")
    return (a + b)

