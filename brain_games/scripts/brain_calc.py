#!/usr/bin/env python
from brain_games.source_logic import run_game
from brain_games.games.brain_calc import brain_calc

TASK = "What is the result of the expression?"


def main():
    run_game(brain_calc, TASK)


if __name__ == "__main__":
    main()
