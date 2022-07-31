from random import randint


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def brain_even():
    number = randint(1, 100)
    if is_even(number):
        return number, "yes"
    return number, "no"
