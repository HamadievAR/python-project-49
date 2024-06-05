#!/usr/bin/env python3
"""Check even."""

from brain_games.games import brain_even
from brain_games import engine


def main():
    """Running the brain-even."""
    engine.run_game_engine(brain_even.DESCRIPTION, brain_even.generate_even_question_and_answer)


if __name__ == '__main__':
    main()
