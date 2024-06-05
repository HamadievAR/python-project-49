"""Command line interface."""

import prompt


def welcome_user():
    """Welcome the user to the Brain Games and prompt for their name."""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
