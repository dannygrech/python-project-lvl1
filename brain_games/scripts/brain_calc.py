import random
import prompt


def main():
    print('Welcome to The Brain Games!')
    name = prompt.string('May I have your name? ')
    count = 0
    while count <=2:
        operator = random.choice(['+', '-', '*'])
        n1 = random.randrange(21)
        n2 = random.randrange(21)
        question = (f'{n1} {operator} {n2}')
        print('What is result of the expression?')
        print(f'Question:{question}')
        answer = prompt.string('Your answer is:')
        if operator == '+':
            result = n1 + n2
            if str(result) == str(answer):
                print('Correct!')
                count = count + 1
            else: 
                print(f'{answer} is the wrong answer;(. Correct answer is {result}')
                print('Lets try again')
        elif operator == '-':
            result = n1 - n2
            if str(result) == str(answer):
                print('Correct!')
                count = count + 1
            else: 
                print(f'{answer} is the wrong answer;(. Correct answer is {result}')
                print('Lets try again')
        elif operator == '*':
            result = n1 * n2
            if str(result) == str(answer):
                print('Correct!')
                count = count + 1
            else: 
                print(f'{answer} is the wrong answer;(. Correct answer is {result}')
                print('Lets try again')

    print(f'Congratulations, {name}!')




