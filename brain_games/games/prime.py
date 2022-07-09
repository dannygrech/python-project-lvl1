import random
import prompt

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_data():
    k = 0
    question = random.randint(1, 50)
    for i in range(2, question // 2 + 1):
        if question % i == 0:
            k = k + 1
    if k <= 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
