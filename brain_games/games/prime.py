import random


def get_correct_answer(num):
    if num <= 1:
        return 'no'
    if num == 2:
        return 'yes'
    if num % 2 == 0:
        return 'no'
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return 'no'
    return 'yes'


def is_prime_game():
    massage = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_condition = f'{massage}'
    num = random.randint(1, 300)
    quetion = f'Question: {num}\nYour answer: '
    correct_answer = get_correct_answer(num)
    game_dictionary = {
        "game_condition": game_condition,
        "question": quetion,
        "correct_answer": correct_answer
    }
    return game_dictionary
