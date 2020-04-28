#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    a = number % -10
    print("Last digit of", number, "is", a, "and is less than 6 and not 0")
else:
    a = number % 10
    if number % 10 > 5:
        print("Last digit of", number, "is", a, "and is greater than 5")
    elif number % 10 == 0:
        print("Last digit of", number, "is", a, "and is 0")
