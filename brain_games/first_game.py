import prompt
from random import randint


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def is_correct(answer, number):
    if is_even(number) is True and answer == 'yes':
        return 'correct'
    elif is_even(number) is False and answer == 'no':
        return 'correct'
    else:
        return 'wrong'


def get_correct_answer(number):
    if is_even(number) is True:
        return 'yes'
    else:
        return 'no'


def is_even_game():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer_count = 0

    while correct_answer_count < 3:
        number = randint(0, 100)
        answer = prompt.string(f'Question: {number}\nYour answer: ')
        if is_correct(answer, number) == 'wrong':
            correct_answer = get_correct_answer(number)
            print(f'"{answer}" is wrong answer;( . Correct amswer was "{correct_answer}". \n Let\'s try again, {name}!')
            break
        print('Correct!')
        correct_answer_count += 1
    else:
        print(f'Congratulations, {name}!')
