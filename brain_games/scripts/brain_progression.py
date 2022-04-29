import random
import prompt


def main():
    print('Welcome to The Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    count = 0
    while count <= 2:
        x = random.randint(1, 7)
        y = random.randint(22, 25)
        z = random.randint(2, 4)
        list_of_numbers = list(range(x, y, z))
        missing_num_index = random.randint(0, len(list_of_numbers) - 1)
        miss_num = list_of_numbers[missing_num_index]
        list_of_numbers[missing_num_index] = '..'
        print('Question:' + str(list_of_numbers))

        answer = prompt.string('Your answer: ')
        if answer == str(miss_num):
            print('Correct!')
            count = count + 1
        else:
            print(f'{answer} is wrong answer :(. Correct answer was {miss_num}')

    print(f'Congratulations, {name}!')
