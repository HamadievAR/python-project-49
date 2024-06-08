#!/usr/bin/env python
"""Brain-Even Game start."""


from brain_games.engine import run_game_engine
from brain_games.games import even


def main():
    """Start the "Brain-Even Game"."""
    run_game_engine(even.DESCRIPTION,
                    even.generate_question_and_answer)


if __name__ == '__main__':
    main()
