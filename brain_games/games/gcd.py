import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_data():
    n1 = random.randrange(101)
    n2 = random.randrange(101)
    question = n1, n2
    answer = str(math.gcd(n1, n2))
    return question, answer
