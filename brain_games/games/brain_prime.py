import math
import random


def prime():
    NUMBER = random.randint(1, 100)
    NUMBER_SQRT = round(math.sqrt(NUMBER))
    divisors = []
    for i in range(2, NUMBER_SQRT + 1):
        divisors.append(NUMBER % i)
    if NUMBER == 2 or 0 not in divisors:
        return NUMBER, "yes"
    else:
        return NUMBER, "no"
