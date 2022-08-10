import prompt

ROUNDS = 3


def run_game(game_type, task):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    print(task)
    try_count = 0
    while try_count < ROUNDS:
        quiz, correct_answer = game_type()
        print(f"Question: {quiz}")
        user_answer = prompt.string("Your answer is: ")
        if str(correct_answer) == user_answer:
            print("Correct!")
            try_count += 1
        else:
            print(f"""\"{user_answer}\" is wrong answer ;(.\
 Correct answer was \"{correct_answer}\".\nLet's try again, {name}!""")
            return
    print(f"""Congratulations, {name}!""")
    return
