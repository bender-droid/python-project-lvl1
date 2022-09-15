from random import randint
from brain_games.brain_engine import run_game

TASK = "Find the greatest common divisor of given numbers."
RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100


def find_gcd(num_1, num_2):
    while num_2 > 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1


def brain_gcd():
    number_1 = randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    number_2 = randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    quiz = f"{number_1} {number_2}"
    result = find_gcd(number_1, number_2)
    return quiz, str(result)


def run_brain_gcd():
    run_game(brain_gcd, TASK)
