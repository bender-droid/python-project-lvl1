from random import randint


def find_gcd(num_1, num_2):
    while num_2 > 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1


def brain_gcd():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    quiz = f"{number_1} {number_2}"
    result = find_gcd(number_1, number_2)
    return quiz, result
