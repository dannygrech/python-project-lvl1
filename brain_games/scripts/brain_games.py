import prompt


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return name


if __name__ == '__main__':
    main()
