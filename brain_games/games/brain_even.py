import random
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_needed = 3
    correct_answers_count = 0

    while correct_answers_count < correct_answers_needed:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if number % 2 == 0 else "no"

        if user_answer == "yes" or user_answer == "no":
            if user_answer == correct_answer:
                print("Correct!")
                correct_answers_count += 1
            else:
                print(f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                return
        else:
            print("Incorrect input. Please enter 'yes' or 'no'.")
            continue

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
