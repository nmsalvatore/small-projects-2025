import unittest

from wod import get_wod, Workout


WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


class TestWod(unittest.TestCase):
    """Test cases for workout generator"""

    def test_long_walk_days(self):
        days = ["Saturday"]
        self._check_wod_by_days(days, Workout.LONG_WALK)

    def test_short_walk_days(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
        self._check_wod_by_days(days, Workout.SHORT_WALK)

    def test_gym_days(self):
        days = ["Friday", "Sunday"]
        self._check_wod_by_days(days, Workout.GYM)

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            get_wod("Saturday")

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            get_wod(-1)
        with self.assertRaises(ValueError):
            get_wod(7)

    def _check_wod_by_days(self, days: list[str], workout: str):
        """Check the provided days return the correct workout"""
        for day in days:
            index = WEEKDAYS.index(day)
            self.assertEqual(get_wod(index), workout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
