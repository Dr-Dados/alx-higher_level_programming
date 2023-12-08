#!/usr/bin/python3
""" module for Base """


class Base:
    """ class Base """
    __nb_objects = 0
    def __init__(self, id = None):
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
            
