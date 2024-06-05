#!/usr/bin/env python3
"""Calculator."""

from brain_games.games import brain_calc
from brain_games import engine


def main():
    """Running the brain-calc."""
    engine.run_game_engine(brain_calc.DESCRIPTION, brain_calc.generate_question_and_answer)


if __name__ == '__main__':
    main()
