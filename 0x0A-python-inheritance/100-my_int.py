#!/usr/bin/python3
"""class"""

class MyInt(int):
    """class body"""
    def __eq__(self, other):
        """ Invert the behavior of =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """ Invert the behavior of !="""
        return super().__eq__(other)
