#!/usr/bin/env python
from brain_games.source_logic import welcome_user, cycle
from brain_games.games.brain_gcd import gcd

task = "Find the greatest common divisor of given numbers."
name = welcome_user()


def main():
    cycle(gcd, name, task)


if __name__ == "__main__":
    main()
