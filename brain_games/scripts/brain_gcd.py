#!/usr/bin/env python
from brain_games.source_logic import run_game
from brain_games.games.brain_gcd import gcd

TASK = "Find the greatest common divisor of given numbers."


def main():
    run_game(gcd, TASK)


if __name__ == "__main__":
    main()
