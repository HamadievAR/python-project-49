import random
from brain_games.cli import welcome_user


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_game():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    answer = input('Your answer: ').lower()
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f'Wrong answer ;(. Correct answer was {correct_answer}.')
        return False


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers_needed = 3
    correct_answers_count = 0

    while correct_answers_count < correct_answers_needed:
        if prime_game():
            correct_answers_count += 1
        else:
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
