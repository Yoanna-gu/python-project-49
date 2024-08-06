from random import randint


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_correct_answer(number):
    if is_even(number) is True:
        return 'yes'
    else:
        return 'no'


def is_even_game():
    message = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_condition = f'{message}'
    number = randint(0, 100)
    quetion = f'Question: {number}\nYour answer: '
    correct_answer = get_correct_answer(number)
    game_dictionary = {
        "game_condition": game_condition,
        "question": quetion,
        "correct_answer": correct_answer
    }
    return game_dictionary
