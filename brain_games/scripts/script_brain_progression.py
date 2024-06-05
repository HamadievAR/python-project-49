#!/usr/bin/env python3
"""Arithmetic progression."""

from brain_games.games import brain_progression
from brain_games import engine


def main():
    """Running the brain-progession."""
    engine.run_game_engine(brain_progression.DESCRIPTION, brain_progression.generate_question_and_answer)


if __name__ == '__main__':
    main()
