import random
from brain_games.cli import welcome_user

OPERATORS = ['+', '-', '*']


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(OPERATORS)
    expression = f"{num1} {operator} {num2}"
    if operator == '+':
        correct_answer = str(num1 + num2)
    elif operator == '-':
        correct_answer = str(num1 - num2)
    else:  # operator == '*'
        correct_answer = str(num1 * num2)
    return expression, correct_answer


def main():
    name = welcome_user()
    print("What is the result of the expression?")

    correct_answers_needed = 3
    correct_answers_count = 0

    while correct_answers_count < correct_answers_needed:
        expression, correct_answer = generate_question()
        print(f"Question: {expression}")
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_answer:
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
