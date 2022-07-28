#!/usr/bin/env python
from brain_games.source_logic import run_game
from brain_games.games.brain_progression import progression

TASK = "What number is missing in the progression?"


def main():
    run_game(progression, TASK)


if __name__ == "__main__":
    main()
