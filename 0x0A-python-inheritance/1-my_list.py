#!/usr/bin/python3
""" a module that prints a list in ascending order"""


class Mylist(list):
    """ a class that inherits from list class"""
    pass

    def print_sorted(self):
        """a method that sort a list"""
        print(sorted(list(self)))
