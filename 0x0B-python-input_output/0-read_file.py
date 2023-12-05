#!/usr/bin/python3
""" module """


def read_file(filename=""):
    """ function """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
