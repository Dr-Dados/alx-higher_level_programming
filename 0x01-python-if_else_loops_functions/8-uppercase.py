#!/usr/bin/python3
def uppercase(s):
    for el in s:
        if (ord(el) >= 97 and ord(el) <= 122):
            el = chr(ord(el) - 32)
        print("{}".format(el), end="")
    print("")
