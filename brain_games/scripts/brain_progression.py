import random
from brain_games.engine import run_game


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, hidden_value


def generate_question_and_answer():
    progression, hidden_value = generate_progression()
    question = ' '.join(map(str, progression))
    correct_answer = str(hidden_value)
    return question, correct_answer


def main():
    description = 'What number is missing in the progression?'
    run_game(description, generate_question_and_answer)


if __name__ == '__main__':
    main()
