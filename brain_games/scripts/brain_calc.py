#!/usr/bin/env python
from brain_games.source_logic import welcome_user, cycle

task = "What is the result of the expression?"
name = welcome_user()


def main():
    cycle("calc", name, task)


if __name__ == "__main__":
    main()
