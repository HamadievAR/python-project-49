import random
from brain_games.cli import welcome_user


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, hidden_value


def progression_game():
    progression, hidden_value = generate_progression()
    progression_str = ' '.join(map(str, progression))
    print(f'Question: {progression_str}')
    answer = input('Your answer: ')
    return answer, hidden_value


def main():
    name = welcome_user()
    print('What number is missing in the progression?')

    correct_answers_needed = 3
    correct_answers_count = 0

    while correct_answers_count < correct_answers_needed:
        answer, hidden_value = progression_game()
        if answer == str(hidden_value):
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{hidden_value}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
