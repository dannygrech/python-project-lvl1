import prompt
from brain_games.scripts import brain_games

ROUNDS_COUNT = 3


def run(games):
    print('Welcome to the Brain Games!')
    name = brain_games.main()
    print(games.DESCRIPTION)
    count = ROUNDS_COUNT
    while count:
        question, correct_answer = games.generate_data()
        print(f'Question: {question}')
        right_answer = prompt.string('Your answer: ')
        if right_answer == correct_answer:
            count -= 1
            print('Correct!')
        else:
            print(f'"{right_answer}" is the wrong answer.'
                  f' Correct answer is "{correct_answer}"')
            print(f'Try again,{name}!')
            break
    else:
        print(f'Congratulations, {name}!')
