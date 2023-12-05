#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read file function

    :param filename:
    """
    f = open(filename, 'r', encoding='utf-8')
    print(f.read(), end="")
    f.close()
