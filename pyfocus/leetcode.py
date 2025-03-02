#!/usr/bin/env python3

import random
import textwrap

import requests


class LeetCodeProblemList:
    def __init__(self, difficulty: str):
        self._difficulty: str = difficulty

    def _format_problem(self, problem: dict) -> str:
        """Format problem data into readable string"""

        return textwrap.dedent(f"""\
            Leetcode Problem #{problem["questionFrontendId"]}: {problem["title"]}
            https://leetcode.com/problems/{problem["titleSlug"]}""")

    def random_problem(self) -> str:
        """Select random problem from problem list"""

        response = requests.get(
            f"https://alfa-leetcode-api.onrender.com/problems?difficulty={self._difficulty}&limit=10000"
        )
        response.raise_for_status()
        data = response.json()
        problem_list: list[dict] = data.get("problemsetQuestionList", [])

        if problem_list == []:
            raise ValueError("Could not find key 'problemsetQuestionList' in response data.")

        problem: dict = random.choice(problem_list)
        return self._format_problem(problem)
