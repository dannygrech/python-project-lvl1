import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_data():
    start_num = random.randint(1, 10)
    step_num = random.randint(1, 10)
    stop_num = step_num * 10 + start_num
    array = list(range(start_num, stop_num, step_num))
    miss_num = random.randint(0, 9)
    correct_answer = str(array[miss_num])
    array[miss_num] = '..'
    question = str(array).replace('[', '').replace(']', '').replace("'", '').replace(',', '')
    return question, correct_answer
