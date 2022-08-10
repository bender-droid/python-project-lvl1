from math import sqrt
from random import randint
from brain_games.brain_engine import run_game

TASK = """Answer "yes" if given number is prime. Otherwise answer "no"."""
RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100


def is_prime(number):
    number_sqrt = round(sqrt(number))
    divisors = []
    for i in range(RANDOM_MIN_VALUE + 1, number_sqrt + 1):
        divisors.append(number % i)
    if number == 2 or 0 not in divisors:
        return True
    return False


def brain_prime():
    number = randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    if is_prime(number):
        return number, "yes"
    return number, "no"


def run_brain_prime():
    run_game(brain_prime, TASK)
