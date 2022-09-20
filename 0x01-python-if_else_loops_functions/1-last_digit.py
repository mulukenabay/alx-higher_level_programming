#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = abs(number) % 10
if s < 5:
	print("Last digit of {:d} is {:d} and is greater than 5" .format(number, s))
elif s == 0: 
	print("Last digit of {:d} is {:d} and is zero" .format(number, s))
elif s < 6 and s != 0:
	print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, s))
