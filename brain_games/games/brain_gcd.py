import random
from brain_games.engine import run_game_engine

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    """Вычисление наибольшего общего делителя (НОД) по алгоритму Евклида."""
    while b:
        a, b = b, a % b
    return a


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))
    return question, correct_answer


def main():
    run_game_engine(DESCRIPTION, generate_question_and_answer)
