import random
import prompt
import math


def main():
    print('Welcome to The Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count <=2:
        n1 = random.randrange(101)
        n2 = random.randrange(101)
        print(f'Question: {n1} {n2}')
        answer = prompt.string('Your answer: ')
        right_answer = str(math.gcd(n1, n2))
        if str(answer) == str(right_answer):
            count = count +1
            print('Correct!')
        else:
            print(f'{answer} is wrong answer. Correct answer was {right_answer}.') 
            print(f'Try again, {name}')


    


    print(f'Congratulations, {name}!')


  