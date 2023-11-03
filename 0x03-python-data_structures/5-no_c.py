#!/usr/bin/python3
def no_c(my_string):
    newString = []
    for el in range(0, len(my_string)):
        if (my_string[el] != 'c' and my_string[el] != 'C'):
            newString.append(my_string[el])
    return "".join(newString)
