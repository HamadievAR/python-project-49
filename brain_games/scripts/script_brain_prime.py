#!/usr/bin/env python
"""Brain Prime Game start."""


from brain_games.engine import run_game_engine
from brain_games.games import brain_prime


def main():
    """Start the "Brain-Prime Game"."""
    run_game_engine(brain_prime.DESCRIPTION,
                    brain_prime.generate_question_and_answer)


if __name__ == '__main__':
    main()
