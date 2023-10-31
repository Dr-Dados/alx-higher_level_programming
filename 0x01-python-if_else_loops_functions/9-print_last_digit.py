#!/usr/bin/python3
def print_last_digit(n):
    lastD = abs(n) % 10
    print("{}".format(lastD), end="")
    return lastD
