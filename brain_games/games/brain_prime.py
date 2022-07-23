import math
import random


def prime():
    number = random.randint(1, 100)
    sqrt_number = round(math.sqrt(number))
    divisors = []
    for i in range(2, sqrt_number + 1):
        divisors.append(number % i)
    if number == 2 or 0 not in divisors:
        return number, "yes"
    else:
        return number, "no"
