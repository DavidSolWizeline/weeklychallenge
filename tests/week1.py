""" Create tests for the week1 function in week1/solution.py file"""
import unittest

from week1.solution import week1


class TestWeek1(unittest.TestCase):
    """Test class for week1.py"""

    def test_no_interval(self):
        self.assertListEqual(week1([]), [], "The result should be an empty list")

    def test_one_interval(self):
        self.assertListEqual(
            week1([(1, 2)]), [1], "The result should be the start of the only interval"
        )

    def same_intervals(self):
        self.assertListEqual(
            week1([(1, 2), (1, 2)]),
            [1],
            "The result should be the start of the intervals",
        )

    def test_two_non_intersecting_intervals(self):
        self.assertListEqual(
            week1([(1, 2), (3, 4)]),
            [1, 3],
            "The result should be the start of each interval",
        )

    def test_three_non_intersecting_intervals(self):
        self.assertListEqual(
            week1([(1, 2), (3, 4), (5, 6)]),
            [1, 3, 5],
            "The result should be the start of each interval",
        )

    def test_one_interval_completely_contained_in_another(self):
        self.assertListEqual(
            week1([(1, 4), (2, 3)]),
            [2],
            "The result should be the start of the smaller interval",
        )

    def test_one_interval_contained_at_the_start_of_another(self):
        self.assertListEqual(
            week1([(1, 4), (1, 3)]),
            [1],
            "The result should be the start of the intervals",
        )

    def test_one_interval_contained_at_the_end_of_another(self):
        self.assertListEqual(
            week1([(1, 4), (2, 4)]),
            [2],
            "The result should be the start of the smaller interval",
        )

    def test_one_interval_intersecting_at_the_start_of_another(self):
        self.assertListEqual(
            week1([(2, 4), (1, 3)]),
            [2],
            "The result should be the start of the first interval",
        )

    def test_one_interval_intersecting_at_the_end_of_another(self):
        self.assertListEqual(
            week1([(1, 3), (2, 4)]),
            [2],
            "The result should be the start of the second interval",
        )

    def test_many_intervals(self):
        self.assertListEqual(
            week1([(4, 8), (3, 4), (7, 9), (1, 2), (10, 12), (11, 11)]),
            [1, 3, 7, 11],
            "The result should be [1, 3, 7, 11]",
        )
