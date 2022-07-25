#!/usr/bin/env python
from brain_games.source_logic import welcome_user, cycle
from brain_games.games.brain_prime import prime

task = """Answer "yes" if given number is prime. Otherwise answer "no"."""
name = welcome_user()


def main():
    cycle(prime, name, task)


if __name__ == "__main__":
    main()
