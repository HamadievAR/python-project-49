#!/usr/bin/env python3
"""Unified script for all brain games."""

import sys
from brain_games import engine
from brain_games.games import (
    brain_calc,
    brain_even,
    brain_gcd,
    brain_prime,
    brain_progression
)


def choose_game(game_name):
    """Choose the game to run based on its name."""
    games = {
        'brain-calc': (brain_calc.DESCRIPTION,
                       brain_calc.generate_question_and_answer),
        'brain-even': (brain_even.DESCRIPTION,
                       brain_even.generate_even_question_and_answer),
        'brain-gcd': (brain_gcd.DESCRIPTION,
                      brain_gcd.generate_question_and_answer),
        'brain-prime': (brain_prime.DESCRIPTION,
                        brain_prime.generate_prime_question_and_answer),
        'brain-progression': (brain_progression.DESCRIPTION,
                              brain_progression.generate_question_and_answer)
    }
    return games.get(game_name)


def main():
    # Check if the game name argument is provided
    if len(sys.argv) != 2:
        sys.exit(1)

    # Get the game name from the command line arguments
    game_name = sys.argv[1]

    # Run the chosen game if the name is known
    game_info = choose_game(game_name)
    if game_info:
        description, generator = game_info
        engine.run_game_engine(description, generator)


if __name__ == '__main__':
    main()
