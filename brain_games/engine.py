import prompt


def start_game(function):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    game_dictionary = function()
    game_condition = game_dictionary['game_condition']
    print(game_condition)
    correct_answer_count = 0

    while correct_answer_count < 3:
        game_dictionary = function()
        question = game_dictionary['question']
        correct_answer = game_dictionary['correct_answer']
        answer = prompt.string(question)
        if answer != correct_answer:
            print(f'"{answer}" is wrong answer;( . Correct amswer was "{correct_answer}". \n Let\'s try again, {name}!')
            break
        print('Correct!')
        correct_answer_count += 1
    else:
        print(f'Congratulations, {name}!')
