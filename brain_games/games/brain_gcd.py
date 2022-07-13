#!/usr/bin/env python
import prompt
import random

print("Welcome to the Brain Games!")
name = prompt.string("May I have your name? ")
print(f"Hello, {name}")
try_count = 0


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


while try_count != 3:
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    print("Find the greatest common divisor of given numbers.")
    print(f""""Question: "{first_num} {second_num}""")
    result = gcd(first_num, second_num)
    guess = int(input("Your answer: "))
    if guess == result:
        print("Correct!")
        try_count += 1
    else:
        print(f"'{guess}' is wrong answer ;(.\
 Correct answer was '{result}'.\nLet's try again, {name}!")
        break
if try_count == 3:
    print(f"Congratulations, {name}!")


def main():
    gcd(first_num, second_num)


if __name__ == "__main__":
    main()
