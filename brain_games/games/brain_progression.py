import random
import prompt


def progression():
    sequence_start = random.randint(1, 80)
    sequence_step = random.randint(1, 6)
    sequence_length = random.randint(8, 13)
    sequence_stop = sequence_start + (sequence_length - 1) * sequence_step
    sequence = []
    for i in range(sequence_start, sequence_stop + 1, sequence_step):
        sequence.append(i)
    return sequence


def question(list):
    hid_num_index = random.randint(0, len(list) - 1)
    hidden_number = ".."
    correct_answer = list[hid_num_index]
    list[hid_num_index] = hidden_number
    question = " ".join(map(str, list))
    return question, correct_answer


def main():
    progression()


print("Welcome to the Brain Games!")
name = prompt.string("May I have your name? ")
print(f"Hello, {name}")
try_count = 0
while try_count != 3:
    some_list = progression()
    quiz, correct_answer = question(some_list)
    print("What number is missing in the progression?")
    print(f"Question: {quiz}")
    guess = int(input("Your answer: "))
    if guess == int(correct_answer):
        print("Correct!")
        try_count += 1
    else:
        print(f"'{guess}' is wrong answer ;(.\
 Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
        break
if try_count == 3:
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
