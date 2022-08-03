from random import randint
from brain_games.brain_engine import run_game

TASK = """Answer "yes" if the number is even, otherwise answer "no"."""
BOTTOM_NUM = 1
TOP_NUM = 100


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def brain_even():
    number = randint(BOTTOM_NUM, TOP_NUM)
    if is_even(number):
        return number, "yes"
    return number, "no"


def run_brain_even():
    run_game(brain_even, TASK)
