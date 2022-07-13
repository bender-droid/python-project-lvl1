#!/usr/bin/env python

import random
import prompt

print("Welcome to the Brain Games!")
name = prompt.string("May I have your name? ")
print(f"Hello, {name}")

operators = "+-*"
try_count = 0


def sum(a, b):
    return a + b


def substr(a, b):
    return a - b


def multiply(a, b):
    return a * b


def calc():
    if operator == "+":
        return sum(first_operand, second_operand)
    elif operator == "-":
        return substr(first_operand, second_operand)
    elif operator == "*":
        return multiply(first_operand, second_operand)


while try_count != 3:
    first_operand = random.randint(0, 100)
    operator = operators[random.randint(0, 2)]
    second_operand = random.randint(0, 100)
    print("What is the result of the expression?")
    print(f"Question: {first_operand} {operator} {second_operand}")
    result = calc()
    guess = int(input("Your answer: "))
    if guess == result:
        print("Correct!")
        try_count += 1
    else:
        print(f"'{guess}' is wrong answer ;(. Correct answer\
  was '{result}'.\nLet's try again, {name}!")
        break
if try_count == 3:
    print(f"Congratulations, {name}!")


def main():
    calc()


if __name__ == "__main__":
    main()
