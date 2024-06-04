import random
from brain_games.engine import run_game


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer


def main():
    description = ('Answer "yes" if given number is prime. '
                   'Otherwise answer "no".')
    run_game(description, generate_question_and_answer)


if __name__ == '__main__':
    main()