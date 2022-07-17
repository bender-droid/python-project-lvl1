import math
import random
import prompt

print("Welcome to the Brain Games!")
name = prompt.string("May I have your name? ")
print(f"Hello, {name}")
try_count = 0


def is_prime():
    number = random.randint(1, 100)
    sqrt_number = round(math.sqrt(number))
    dividors = []
    for i in range(2, sqrt_number + 1):
        dividors.append(number % i)
    if number == 2 or 0 not in dividors:
        return number, True
    else:
        return number, False


while try_count != 3:
    print("""Answer "yes" if given number is prime. Otherwise answer "no".""")
    question, result = is_prime()
    print(f"Question: {question}")
    guess = input("Your answer: ")
    if (result and guess == "yes") or (not result and guess == "no"):
        print("Correct!")
        try_count += 1
    elif result and guess == "no":
        print(f"'no' is wrong answer ;(.\
 Correct answer was 'yes'.\nLet's try again, {name}!")
        break
    else:
        print(f"'yes' is wrong answer ;(.\
 Correct answer was 'no'.\nLet's try again, {name}!")
        break

if try_count == 3:
    print(f"Congratulations, {name}!")


def main():
    is_prime()


if __name__ == "__main__":
    main()
