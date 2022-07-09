import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_data():
    x = random.randint(1, 7)
    y = random.randint(22, 25)
    z = random.randint(2, 4)
    list_of_numbers = list(range(x, y, z))
    missing_num_index = random.randint(0, len(list_of_numbers) - 1)
    miss_num = list_of_numbers[missing_num_index]
    list_of_numbers[missing_num_index] = '..'
    question = list_of_numbers
    answer = str(miss_num)
    return question, answer
