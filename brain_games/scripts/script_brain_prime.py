#!/usr/bin/env python3
"""Prime numbers."""

from brain_games.games import brain_prime
from brain_games import engine


def main():
    """Running the brain-prime."""
    engine.run_game_engine(brain_prime.DESCRIPTION, brain_prime.generate_question_and_answer)


if __name__ == '__main__':
    main()
