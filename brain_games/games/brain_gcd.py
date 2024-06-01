import random
from brain_games.cli import welcome_user


def gcd(a, b):
    """Вычисление наибольшего общего делителя (НОД) по алгоритму Евклида."""
    while b:
        a, b = b, a % b
    return a


def main():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    correct_answers_needed = 3
    correct_answers_count = 0

    while correct_answers_count < correct_answers_needed:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Question: {num1} {num2}")

        correct_answer = gcd(num1, num2)
        user_answer = input("Your answer: ").strip()

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
