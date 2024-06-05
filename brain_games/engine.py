"""Games Engine."""

from brain_games.cli import welcome_user


CORRECT_ANSWERS_NEEDED = 3


def run_game_engine(description, generate_question_and_answer):
    name = welcome_user()
    print(description)

    correct_answers_count = 0

    while correct_answers_count < CORRECT_ANSWERS_NEEDED:
        question, correct_answer = generate_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
