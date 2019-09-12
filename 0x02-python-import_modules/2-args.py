#!/usr/bin/python3
import sys
count = 0
f = 0
if len(sys.argv) == 2:
    print("{:d} argument:".format(len(sys.argv) - 1))
elif len(sys.argv) == 1:
    print("{:d} arguments.".format(len(sys.argv) - 1))
else:
    print("{:d} arguments:".format(len(sys.argv) - 1))
for elemen in sys.argv:
    if count != 0:
        print("{:d}: {:s}".format(count, elemen))
        count += 1
        f = 1
    if f == 0:
        count += 1
