#!/usr/bin/python3
import sys
if (len(sys.argv) == 1):
    print("0 arguments.")
else:
    if (len(sys.argv) == 2):
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for el in range(1, len(sys.argv)):
        print("{}: {}".format(el, sys.argv[el]))
