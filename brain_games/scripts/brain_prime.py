#!/usr/bin/env python
from brain_games.source_logic import run_game
from brain_games.games.brain_prime import prime

TASK = """Answer "yes" if given number is prime. Otherwise answer "no"."""


def main():
    run_game(prime, TASK)


if __name__ == "__main__":
    main()
