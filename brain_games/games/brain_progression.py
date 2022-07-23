import random


def progression():
    sequence_start = random.randint(1, 80)
    sequence_step = random.randint(1, 6)
    sequence_length = random.randint(8, 13)
    sequence_stop = sequence_start + (sequence_length - 1) * sequence_step
    sequence = []
    for i in range(sequence_start, sequence_stop + 1, sequence_step):
        sequence.append(i)
    hid_num_index = random.randint(0, len(sequence) - 1)
    hidden_number = ".."
    correct_answer = sequence[hid_num_index]
    sequence[hid_num_index] = hidden_number
    question = " ".join(map(str, sequence))
    return question, correct_answer
