from random import randint


def brain_calc():
    operators = "+-*"
    operand_1 = randint(1, 100)
    operator = operators[randint(0, 2)]
    operand_2 = randint(1, 100)
    quiz = f"{operand_1} {operator} {operand_2}"
    if operator == "+":
        correct_answer = operand_1 + operand_2
    elif operator == "-":
        correct_answer = operand_1 - operand_2
    elif operator == "*":
        correct_answer = operand_1 * operand_2
    return quiz, correct_answer
