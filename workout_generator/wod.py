from datetime import date
from enum import StrEnum


class Workout(StrEnum):
    """Defines workout types"""

    SHORT_WALK = "Go on a short walk"
    LONG_WALK = "Go on a long walk"
    GYM = "Go to the gym"
    DEFAULT = "Run for the hills because time is a flat circle"


def get_wod(weekday: int) -> str:
    """Determines a workout based on the supplied day

    Args:
        weekday (int): Day of the week (0-6, Monday-Sunday)

    Returns:
        str: The workout for the given day
    """

    match weekday:
        case 0 | 1 | 2 | 3:
            return Workout.SHORT_WALK
        case 5:
            return Workout.LONG_WALK
        case 4 | 6:
            return Workout.GYM
        case _:
            return Workout.DEFAULT


if __name__ == "__main__":
    today = date.today()
    print(get_wod(today.weekday()))
