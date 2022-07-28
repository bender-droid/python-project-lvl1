import prompt


def run_game(game_type, TASK, rounds=3):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    print(TASK)
    try_count = 0
    while try_count < rounds:
        quiz, correct_answer = game_type()
        print(f"Question: {quiz}")
        user_answer = prompt.string("Your answer is: ")
        if str(correct_answer) == user_answer:
            print("Correct")
            try_count += 1
        else:
            return print(f"""\"{user_answer}\" is wrong answer ;(.\
 Correct answer was \"{correct_answer}\".\nLet's try again, {name}!""")
    return print(f"""Congratulations, {name}!""")
