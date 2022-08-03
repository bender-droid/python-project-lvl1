from random import randint
from brain_games.brain_engine import run_game

TASK = "What number is missing in the progression?"


def brain_progression():
    seq_start = randint(1, 80)
    seq_step = randint(1, 6)
    seq_length = randint(8, 13)
    seq_stop = seq_start + (seq_length - 1) * seq_step
    sequence = []
    for i in range(seq_start, seq_stop + 1, seq_step):
        sequence.append(i)
    hid_num_index = randint(0, len(sequence) - 1)
    hidden_number = ".."
    correct_answer = sequence[hid_num_index]
    sequence[hid_num_index] = hidden_number
    question = " ".join(map(str, sequence))
    return question, correct_answer


def run_brain_progression():
    run_game(brain_progression, TASK)
