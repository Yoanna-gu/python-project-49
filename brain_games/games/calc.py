import random
import operator


def get_correct_answer(num1, num2, op):
    if op == '-':
        answer = num1 - num2
    elif op == '+':
        answer = num1 + num2
    else:
        answer = num1 * num2
    return answer

def calc_game():
    game_condition = f'What is the result of the expression?'
    operator = ['-', '+', '*']
    op = random.choice(operator)
    num1 = random.randint(10, 30)
    num2 = random.randint(1, 10)
    expression = f'{num1}{op}{num2}'
    quetion = f'Question: {expression}\nYour answer: '
    correct_answer = str(get_correct_answer(num1, num2, op))
    game_dictionary = {
        "game_condition": game_condition,
        "question": quetion,
        "correct_answer": correct_answer
    }
    return game_dictionary