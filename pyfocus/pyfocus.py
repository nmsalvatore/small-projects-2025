#!/usr/bin/env python3

import random

from enum import StrEnum


class FocusOptions(StrEnum):
    READ = "Read a chapter in Dead Simple Python."
    WRITE = "Write a blog post about a Python concept."
    SMALL_PROJECT = "Build a small Python project."
    LARGE_PROJECT = "Work on movie scraper."
    LEETCODE = "Do a Leetcode problem."


def get_leetcode_problem() -> str | None:
    try:
        from leetcode import LeetCodeProblemList
        problem_list = LeetCodeProblemList("EASY")
        return problem_list.random_problem()
    except:
        return None


def get_focus_task() -> str:
    focus = random.choice(list(FocusOptions))
    if focus.name == "LEETCODE":
        problem = get_leetcode_problem()
        if problem:
            return problem
    return focus


if __name__ == "__main__":
    print(get_focus_task())
