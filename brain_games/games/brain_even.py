from random import randint
from brain_games.brain_engine import run_game

TASK = """Answer "yes" if the number is even, otherwise answer "no"."""
RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def brain_even():
    number = randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    if is_even(number):
        return number, "yes"
    return number, "no"


def run_brain_even():
    run_game(brain_even, TASK)
