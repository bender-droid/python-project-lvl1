from random import randint, choice
from brain_games.brain_engine import run_game

TASK = "What is the result of the expression?"
RANDOM_MIN_VALUE = 1
RANDOM_MAX_VALUE = 100


def brain_calc():
    operators = "+-*"
    operand_1 = randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    operator = choice(operators)
    operand_2 = randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    quiz = f"{operand_1} {operator} {operand_2}"
    if operator == "+":
        correct_answer = operand_1 + operand_2
    elif operator == "-":
        correct_answer = operand_1 - operand_2
    elif operator == "*":
        correct_answer = operand_1 * operand_2
    return quiz, correct_answer


def run_brain_calc():
    run_game(brain_calc, TASK)
