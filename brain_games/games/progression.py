import random

DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10


def get_question(init_value, step_value, hidden_index):
    question = ''
    count = 0
    while count < PROGRESSION_LENGTH:
        if count > 0:
            question += ' '
        if count == hidden_index:
            question += '..'
        else:
            question += str(init_value + step_value * count)
        count += 1
    return question


def generate_data():
    init_value = random.randint(1, 10)
    step_value = random.randint(1, 10)
    hidden_index = random.randint(0, 9)
    question = get_question(init_value, step_value, hidden_index)
    correct_answer = str(step_value * hidden_index + init_value)
    return question, correct_answer
