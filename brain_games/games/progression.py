import random


def progression_game():
    game_condition = f'What number is missing in the progression?'
    next_num = random.randint(1, 30)
    step = random.randint(1, 5)
    progression = []
    lenght = 10
    while lenght != 0:
        progression.append(next_num)
        next_num += step
        lenght -= 1
    x_num_index = random.randint(0, 9)
    correct_answer = str(progression[x_num_index])
    progression[x_num_index] = '..'
    progression_str = []
    for element in progression:
        element = str(element)
        progression_str.append(element)
    nums = ' '.join(progression_str)
    quetion = f'Question: {nums}\nYour answer: '
    game_dictionary = {
        "game_condition": game_condition,
        "question": quetion,
        "correct_answer": correct_answer
    }
    return game_dictionary
