import random
import prompt


def main():
    print('Welcome to The Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count <= 2:
        k = 0
        number = random.randint(1, 50)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        for i in range(2, number // 2 + 1):
            if (number % i == 0):
                k = k + 1
        if k <= 0:
            result = 'prime'
        else:
            result = 'not_prime'

        if result == 'prime' and answer == 'yes':
            print('Correct!')
            count = count + 1
        elif result == 'not_prime' and answer == 'no':
            print('Correct!')
            count = count + 1
        else:
            print(f'Try again, {name}')
            quit()

    print(f'Congratulations, {name}!')
