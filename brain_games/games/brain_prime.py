from math import sqrt
from random import randint
from brain_games.brain_engine import run_game

TASK = """Answer "yes" if given number is prime. Otherwise answer "no"."""
BOTTOM_NUM = 1
TOP_NUM = 100


def is_prime(number):
    number_sqrt = round(sqrt(number))
    divisors = []
    for i in range(BOTTOM_NUM + 1, number_sqrt + 1):
        divisors.append(number % i)
    if number == 2 or 0 not in divisors:
        return True
    return False


def brain_prime():
    number = randint(BOTTOM_NUM, TOP_NUM)
    if is_prime(number):
        return number, "yes"
    return number, "no"


def run_brain_prime():
    run_game(brain_prime, TASK)
