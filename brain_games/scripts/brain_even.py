#!/usr/bin/env python
from brain_games.source_logic import welcome_user, cycle
from brain_games.games.brain_even import even


task = """Answer "yes" if the number is even, otherwise answer "no"."""
name = welcome_user()


def main():
    cycle(even, name, task)


if __name__ == "__main__":
    main()
