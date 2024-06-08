#!/usr/bin/env python
"""Brain-GCD Game start."""


from brain_games.engine import run_game_engine
from brain_games.games import gcd


def main():
    """Start the "Brain-GCD Game"."""
    run_game_engine(gcd.DESCRIPTION,
                    gcd.generate_question_and_answer)


if __name__ == '__main__':
    main()
