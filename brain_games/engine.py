import prompt

from brain_games.scripts import brain_games

ROUNDS_COUNT = 3


def run(games):
    print(games.DESCRIPTION)
    count = ROUNDS_COUNT
    name = brain_games.main()
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
<<<<<<< HEAD
        print(f"Congratulations, {name}!")
=======
            
print(f'Congratulations, {name}!')
>>>>>>> refs/remotes/origin/main
