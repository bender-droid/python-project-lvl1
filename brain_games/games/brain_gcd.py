#!/usr/bin/env python
import random


def gcd():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    quiz = (f"{first_num} {second_num}")
    while second_num > 0:
        first_num, second_num = second_num, first_num % second_num
    return quiz, first_num
