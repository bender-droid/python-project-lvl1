#!/usr/bin/env python
from brain_games.source_logic import run_game
from brain_games.games.brain_even import brain_even

TASK = """Answer "yes" if the number is even, otherwise answer "no"."""


def main():
    run_game(brain_even, TASK)


if __name__ == "__main__":
    main()
