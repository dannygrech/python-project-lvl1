import operator
import random

DESCRIPTION = 'What is the result of the expression?'


def calc(num1, num2, operator_action):
    return operator_action(num1, num2)


def generate_data():
    operators = (('+', operator.add), ('-', operator.sub), ('*', operator.mul))
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operators_symbol, operator_action = random.choice(operators)
    question = f'{num1} {operators_symbol} {num2}'
    correct_answer = str(calc(num1, num2, operator_action))
    return question, correct_answer
