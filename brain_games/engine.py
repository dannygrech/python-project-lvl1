import prompt


ROUNDS_COUNT = 3


def run(games):
    print('Welcome to the Brain Games!!!!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count = ROUNDS_COUNT
    print(games.DESCRIPTION)
    while count:
        question, correct_answer = games.generate_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            count -= 1
            print('Correct!')
        else:
            print(f'"{answer}" is the wrong answer.'
                  f' Correct answer is "{correct_answer}"')
            print(f'Try again,{name}!')
            break
        print(f"Congratulations, {name}!")
