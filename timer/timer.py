#!/usr/bin/env python3

import argparse
import time
import curses
from curses import wrapper

from nava import play


def timer(stdscr, hours: int, minutes: int, seconds: int):
    if not any((hours, minutes, seconds)):
        minutes = 25

    stdscr.clear()
    curses.curs_set(0)

    start_time = time.time()
    timer_time = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)

    while True:
        elapsed_seconds = int(time.time() - start_time)
        time_remaining = timer_time - elapsed_seconds

        hours = time_remaining // 3600
        minutes = (time_remaining - (hours * 3600)) // 60
        seconds = time_remaining % 60

        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        stdscr.addstr(
            curses.LINES // 2,
            curses.COLS // 2 - len(formatted_time) // 2,
            formatted_time
        )

        if time_remaining < 0:
            break

        time.sleep(0.1)
        stdscr.refresh()

    message = "Time's up! Press any key to exit."
    stdscr.addstr(
        curses.LINES // 2,
        curses.COLS // 2 - len(message) // 2,
        message
    )

    play("bell.wav")

    stdscr.getch()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hours", default=0, help="set timer hours")
    parser.add_argument("--minutes", default=0, help="set timer minutes")
    parser.add_argument("--seconds", default=0, help="set timer seconds")
    args = parser.parse_args()

    wrapper(lambda stdscr: timer(stdscr, args.hours, args.minutes, args.seconds))
