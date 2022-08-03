from random import randint, choice
from brain_games.brain_engine import run_game

TASK = "What is the result of the expression?"
BOTTOM_NUM = 1
TOP_NUM = 100


def brain_calc():
    operators = "+-*"
    operand_1 = randint(BOTTOM_NUM, TOP_NUM)
    operator = choice(operators)
    operand_2 = randint(BOTTOM_NUM, TOP_NUM)
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
