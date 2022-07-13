#!/usr/bin/env python

from random import random
import prompt

print("Welcome to the Brain Games!")
name = prompt.string("May I have your name? ")
print(f"Hello, {name}")


def is_even():
    print("""Answer "yes" if the number is even, otherwise answer "no".""")
    try_count = 0
    while try_count != 3:
        number = round(random() * 100)
        print(f"Question: {number}")
        guess = input("Your answer is: ")
        if (guess == "yes" and number % 2 == 0) or (
                guess == "no" and number % 2 != 0):
            print("Correct!")
            try_count += 1
        elif guess == "yes" and number % 2 != 0:
            print(f""""yes" is wrong answer ;(.\
 Correct answer was "no".\nLet's try again, {name}!""")
            try_count = 0
        elif guess == "no" and number % 2 == 0:
            print(f""""no" is wrong answer ;(.\
 Correct answer was "yes".\nLet's try again, {name}""")
            try_count = 0
        else:
            print("""Sorry, "yes" or "no" answers only!""")
            try_count = 0
    print(f"Congratulations, {name}!")


def main():
    is_even()


if __name__ == "__main__":
    main()
