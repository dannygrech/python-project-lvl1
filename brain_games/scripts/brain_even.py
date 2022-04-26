import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')



    count = 0
    while count <= 2:
        question = random.randint(1, 30)
        print(question)
        
        anwser = prompt.string('Your answer:')
        
        if question % 2 == 0 and anwser == 'yes':
            print('Correct!')
            count = count + 1
        elif question % 2 != 0 and anwser == 'no':
            print('Correct!')
            count = count + 1
        else:
            if anwser != 'yes':
                print(anwser + ' is the wrong answer ;(. Correct answer was "yes".')
                print('Lets try again')
            elif anwser != 'no':
                print(anwser + ' is the wrong answer ;(. Correct answer was "no".')
                print('Lets try again')

    print ('Congratulations, ' + name + '!')

if __name__ == '__main__':
    main()
