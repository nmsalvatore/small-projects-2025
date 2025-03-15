#!/usr/bin/env python3

import random

workouts = [
    {
        "rounds": [2, 3],
        "movements": [
            "20 chin tucks",
            "20 glute bridges"
        ]
    },
    {
        "rounds": [2, 3, 4],
        "movements": [
            "10 pushups",
            f"20 {random.choice(['air squats', 'reverse lunges'])}"
        ]
    },
    {
        "rounds": [2],
        "movements": [
            "20 calf raises",
            "20 tib raises"
        ]
    },
    {
        "rounds": [2, 3],
        "movements": [
            "10 side-lying leg raises, each side",
            "10 side-lying leg circles, each side",
            "10 side-lying leg-circles, opposite direction, each side"
        ]
    },
    {
        "rounds": [2, 3],
        "movements": [
            "10 banded Ws",
            "10 gripper closes",
            "20 banded extensors"
        ]
    },
    {
        "rounds": [2, 3],
        "movements": [
            "10 reverse Nordic curls",
            "10 hip airplanes, each side",
        ]
    },
    {
        "rounds": [3, 4, 5],
        "movements": [
            "10s downward dog",
            "10s cobra"
        ]
    },
    {
        "rounds": [3, 4, 5],
        "movements": [
            "10s forward bend",
            "10s standing chest expansion",
        ]
    },
    {
        "rounds": [2],
        "movements": [
            "10 ulnar nerve flosses",
            "10 medial nerve flosses",
            "10 radial nerve flosses"
        ]
    },
]

workout = random.choice(workouts)
rounds = random.choice(workout["rounds"])

print(f"\nHey! Get up and do {rounds} rounds of:\n")

for movement in workout["movements"]:
    print("  • " + movement)

print()
