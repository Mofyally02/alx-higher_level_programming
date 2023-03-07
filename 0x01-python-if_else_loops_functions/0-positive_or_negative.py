#!/usr/bin/python3
import random
number = random.randint(-10, 10) # assigns a random signed number between -10 and 10 (inclusive) to the variable number
print
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
