#!/usr/bin/env python3

import random


FOCUS_OPTIONS = [
    "Read a chapter in Dead Simple Python",
    "Write a blog post about a Python concept",
    "Write a small Python program",
    "Work on movie scraper",
    "Do a Leetcode problem",
]

focus = random.choice(FOCUS_OPTIONS)
print(focus)
