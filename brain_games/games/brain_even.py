import random
from brain_games.engine import run_game_engine

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_even_question_and_answer():
    number = random.randint(1, 1000)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer


def main():
    run_game_engine(DESCRIPTION, generate_even_question_and_answer)
