#!/usr/bin/env python
"""Brain Progression Game start."""


from brain_games.engine import run_game_engine
from brain_games.games import progression


def main():
    """Start the "Brain-Progression Game"."""
    run_game_engine(progression.DESCRIPTION,
                    progression.generate_question_and_answer)


if __name__ == '__main__':
    main()
