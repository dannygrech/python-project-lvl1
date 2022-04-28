import prompt


ruleslist = {
    'Brain even': 'some rules',
    'Brain Games': 'Another rules'
}


def get_started(game_title: str ='Brain Games') -> str:

    print(f'Welcome to the {game_title}!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(ruleslist[game_title])
    return name


