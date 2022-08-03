from random import randint
from brain_games.brain_engine import run_game

TASK = "Find the greatest common divisor of given numbers."
BOTTOM_NUM = 1
TOP_NUM = 100


def find_gcd(num_1, num_2):
    while num_2 > 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1


def brain_gcd():
    number_1 = randint(BOTTOM_NUM, TOP_NUM)
    number_2 = randint(BOTTOM_NUM, TOP_NUM)
    quiz = f"{number_1} {number_2}"
    result = find_gcd(number_1, number_2)
    return quiz, result


def run_brain_gcd():
    run_game(brain_gcd, TASK)
