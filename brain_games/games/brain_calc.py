import random


def calc():
    operators = "+-*"
    first_operand = random.randint(0, 100)
    operator = operators[random.randint(0, 2)]
    second_operand = random.randint(0, 100)
    if operator == "+":
        quiz = (f"{first_operand} {operator} {second_operand}")
        correct_answer = first_operand + second_operand
        return quiz, correct_answer
    elif operator == "-":
        quiz = (f"{first_operand} {operator} {second_operand}")
        correct_answer = first_operand - second_operand
        return quiz, correct_answer
    elif operator == "*":
        quiz = (f"{first_operand} {operator} {second_operand}")
        correct_answer = first_operand * second_operand
        return quiz, correct_answer
