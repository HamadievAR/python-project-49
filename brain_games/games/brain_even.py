import random
from brain_games.cli import welcome_user


def generate_question():
    number = random.randint(1, 100)
    return number


def check_answer(number, user_answer):
    correct_answer = "yes" if number % 2 == 0 else "no"
    if user_answer == correct_answer:
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_needed = 3
    correct_answers_count = 0

    while correct_answers_count < correct_answers_needed:
        number = generate_question()
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == "yes" or user_answer == "no":
            if check_answer(number, user_answer):
                print("Correct!")
                correct_answers_count += 1
            else:
                print(f"Let's try again, {name}!")
                return
        else:
            print("Incorrect input. Please enter 'yes' or 'no'.")
            continue

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()