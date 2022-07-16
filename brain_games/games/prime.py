import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k = k + 1
    return k <= 0


def generate_data():
    question = random.randint(1, 50)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer


