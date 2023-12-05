#!/usr/bin/python3
""" module """


def read_file(filename=""):
    """ function """
    f = open(filename, 'r', encoding='utf-8')
    print(f.read(), end="")
    f.close()
