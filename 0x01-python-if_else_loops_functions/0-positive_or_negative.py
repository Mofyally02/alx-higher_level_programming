#!/usr/bin/python3
import random
number = random.randint(-10, 10) # assigns a random signed number between -10 and 10 (inclusive) to the variable number
print(number)
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
