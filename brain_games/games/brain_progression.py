import random


def progression():
    SEQ_START = random.randint(1, 80)
    SEQ_STEP = random.randint(1, 6)
    SEQ_LENGTH = random.randint(8, 13)
    SEQ_STOP = SEQ_START + (SEQ_LENGTH - 1) * SEQ_STEP
    sequence = []
    for i in range(SEQ_START, SEQ_STOP + 1, SEQ_STEP):
        sequence.append(i)
    hid_num_index = random.randint(0, len(sequence) - 1)
    hidden_number = ".."
    correct_answer = sequence[hid_num_index]
    sequence[hid_num_index] = hidden_number
    question = " ".join(map(str, sequence))
    return question, correct_answer
