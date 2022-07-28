from random import random


def even():
    NUMBER = round(random() * 100)
    if NUMBER % 2 == 0:
        return NUMBER, "yes"
    return NUMBER, "no"
