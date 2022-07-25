#!/usr/bin/env python
from brain_games.source_logic import welcome_user, cycle
from brain_games.games.brain_progression import progression

task = "What number is missing in the progression?"
name = welcome_user()


def main():
    cycle(progression, name, task)


if __name__ == "__main__":
    main()
