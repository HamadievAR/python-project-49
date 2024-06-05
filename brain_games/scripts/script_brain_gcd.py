#!/usr/bin/env python3
"""Greatest common divisor."""

from brain_games.games import brain_gcd
from brain_games import engine


def main():
    """Running the brain-gcd."""
    engine.run_game_engine(brain_gcd.DESCRIPTION, brain_gcd.generate_question_and_answer)


if __name__ == '__main__':
    main()
