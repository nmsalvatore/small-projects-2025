#!/usr/bin/env python3

import random
import textwrap

import requests


response = requests.get("https://alfa-leetcode-api.onrender.com/problems?difficulty=EASY")
response.raise_for_status()
data = response.json()

problem_list = data.get("problemsetQuestionList")

if problem_list is None:
    raise ValueError("Could not find key 'problemsetQuestionList' is response data.")


class LeetCodeProblem:
    def __init__(self, problem_data):
        self.problem_data = problem_data

    def __str__(self):
        return textwrap.dedent(f"""\
            Leetcode Problem #{self.problem_data["questionFrontendId"]}: {self.problem_data["title"]}
            https://leetcode.com/problems/{self.problem_data["titleSlug"]}""")


problem_choice = random.choice(problem_list)
problem = LeetCodeProblem(problem_choice)
print(problem)
