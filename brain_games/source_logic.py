import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    return name


def cycle(type, name, rounds=3):
    try_count = 0
    while try_count < rounds:
        if type == "even":
            quiz, correct_answer = even()
        elif type == "calc":
            quiz, correct_answer = calc()
        elif type == "progression":
            quiz, correct_answer = progression()
        elif type == "gcd":
            quiz, correct_answer = gcd()
        elif type == "prime":
            quiz, correct_answer = prime()
        else:
            print("Type name is missing or incorrect")
        print(task)
        print(f"Question: {quiz}")
        user_answer = input("Your answer is: ")
        if str(correct_answer) == str(user_answer):
            print("Correct")
            try_count += 1
        else:
            return print(f"""\"{user_answer}\" is wrong answer ;(.\
 Correct answer was \"{correct_answer}\".\nLet's try again, {name}!""")
    return print(f"""Congratulations, {name}!""")
