import random


def gcd():
    NUMBER_1 = random.randint(1, 100)
    NUMBER_2 = random.randint(1, 100)
    quiz = (f"{NUMBER_1} {NUMBER_2}")
    while NUMBER_2 > 0:
        NUMBER_1, NUMBER_2 = NUMBER_2, NUMBER_1 % NUMBER_2
    return quiz, NUMBER_1
