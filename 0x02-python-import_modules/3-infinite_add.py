#!/usr/bin/python3
import sys
result = 0
for el in range(1, len(sys.argv)):
    result += int(sys.argv[el])
print("{}".format(result))
