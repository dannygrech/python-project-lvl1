import prompt
from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def run(games):
    count = ROUNDS_COUNT
    name = welcome_user()
    print(games.DESCRIPTION)
    while count:
        count -= 1
        question, correct_answer = games.generate_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f'"{answer}" is the wrong answer.'
                  f' Correct answer is "{correct_answer}"')
            print(f'Try again,{name}!')
            return

    print(f"Congratulations, {name}!")
