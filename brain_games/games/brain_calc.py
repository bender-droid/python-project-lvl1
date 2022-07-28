import random


def calc():
    operators = "+-*"
    OPERAND_1 = random.randint(0, 100)
    operator = operators[random.randint(0, 2)]
    OPERAND_2 = random.randint(0, 100)
    quiz = (f"{OPERAND_1} {operator} {OPERAND_2}")
    if operator == "+":
        correct_answer = OPERAND_1 + OPERAND_2
    elif operator == "-":
        correct_answer = OPERAND_1 - OPERAND_2
    elif operator == "*":
        correct_answer = OPERAND_1 * OPERAND_2
    return quiz, correct_answer
