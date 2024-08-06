import random
import math


def get_correct_answer(num1, num2):
    answer = math.gcd(num1, num2)
    return answer

def gcd_game():
    game_condition = f'Find the greatest common divisor of given numbers.'
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    expression = f'{num1} {num2}'
    quetion = f'Question: {expression}\nYour answer: '
    correct_answer = str(get_correct_answer(num1, num2))
    game_dictionary = {
        "game_condition": game_condition,
        "question": quetion,
        "correct_answer": correct_answer
    }
    return game_dictionary
