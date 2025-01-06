from datetime import date
from enum import StrEnum


class Workout(StrEnum):
    """Defines workout types"""

    SHORT_WALK = "Go on a short walk"
    LONG_WALK = "Go on a long walk"
    GYM = "Go to the gym"


def get_wod(weekday: int) -> str:
    """Determines a workout based on the supplied day

    Args:
        weekday (int): Day of the week (0-6, Monday-Sunday)

    Returns:
        str: The workout for the given day

    Raises:
        ValueError: if weekday is not an integer between 0 and 6
    """

    if not isinstance(weekday, int):
        raise ValueError("weekday must be an integer")

    if weekday < 0 or weekday > 6:
        raise ValueError("weekday must be an integer between 0 and 6")

    match weekday:
        case 0 | 1 | 2 | 3:
            return Workout.SHORT_WALK
        case 5:
            return Workout.LONG_WALK
        case 4 | 6:
            return Workout.GYM


if __name__ == "__main__":
    today = date.today()
    print(get_wod(today.weekday()))
