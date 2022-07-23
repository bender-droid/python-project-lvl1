from random import random


def even():
    num = round(random() * 100)
    if num % 2 == 0:
        return num, "yes"
    return num, "no"
