#!/usr/bin/python3
"""is same class function"""


def is_same_class(obj, a_class):
    """ isinstance function
    
    :param obj:
    :param a_class:
    """
    return True if type(obj) == a_class else False
