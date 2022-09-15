from random import randint
from brain_games.brain_engine import run_game

TASK = "What number is missing in the progression?"
MIN_SEQ_START = 1
MAX_SEQ_START = 80
MIN_SEQ_STEP = 1
MAX_SEQ_STEP = 6
MIN_SEQ_LENGTH = 8
MAX_SEQ_LENGTH = 13


def brain_progression():
    seq_start = randint(MIN_SEQ_START, MAX_SEQ_START)
    seq_step = randint(MIN_SEQ_STEP, MAX_SEQ_STEP)
    seq_length = randint(MIN_SEQ_LENGTH, MAX_SEQ_LENGTH)
    seq_stop = seq_start + (seq_length - 1) * seq_step
    sequence = []
    for i in range(seq_start, seq_stop + 1, seq_step):
        sequence.append(i)
    hid_num_index = randint(0, len(sequence) - 1)
    hidden_number = ".."
    correct_answer = sequence[hid_num_index]
    sequence[hid_num_index] = hidden_number
    question = " ".join(map(str, sequence))
    return question, str(correct_answer)


def run_brain_progression():
    run_game(brain_progression, TASK)
