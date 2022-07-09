import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_data():
    question = random.randint(1, 30)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
