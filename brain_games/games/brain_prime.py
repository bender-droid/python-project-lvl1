from math import sqrt
from random import randint


def is_prime(number):
    number_sqrt = round(sqrt(number))
    divisors = []
    for i in range(2, number_sqrt + 1):
        divisors.append(number % i)
    if number == 2 or 0 not in divisors:
        return True
    return False


def brain_prime():
    number = randint(1, 100)
    if is_prime(number):
        return number, "yes"
    return number, "no"
