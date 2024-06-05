#!/usr/bin/env python
"""Brain-Calc Game start."""


from brain_games.engine import run_game_engine
from brain_games.games import brain_calc


def main():
    """Start the "Brain-Calc Game"."""
    run_game_engine(brain_calc.DESCRIPTION,
                    brain_calc.generate_question_and_answer)


if __name__ == '__main__':
    main()
