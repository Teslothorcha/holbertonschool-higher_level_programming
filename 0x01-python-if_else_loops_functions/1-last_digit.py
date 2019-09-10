#!/usr/bin/python3
import random
s = "Last digit of "
number = random.randint(-10000, 10000)
if number < 0:
    l = (number * -1) % 10
else:
    l = number % 10
if l > 5:
    print('{:s}{:d} is {:d} and is greater than 5'.format(s, number, l))
elif l == 0:
    print('{:s}{:d} is {:d} and is 0'.format(s, number, l))
else:
    print('{:s}{:d} is {:d} and is less than 6 and not 0'.format(s, number, l))
