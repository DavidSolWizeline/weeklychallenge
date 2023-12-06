""" Create tests for the week5 function in week5/solution.py file"""
import unittest

from week5.solution import week5


class TestWeek5(unittest.TestCase):
    """Test class for week5.py"""

    def test_no_data(self):
        self.assertEqual(week5([]), -1, "If no data returns -1")

    def test_no_individual(self):
        self.assertEqual(
            week5([3, 5, 6, 5, 6, 3]), -1, "If no individual integer returns -1"
        )

    def test_individual_biggest(self):
        self.assertEqual(
            week5([9, 3, 5, 6, 5, 6, 3]), 9, "The individual 9 at the start"
        )

    def test_individual_smallest(self):
        self.assertEqual(
            week5([9, 3, 5, 6, 5, 6, 3, 9, 1]), 1, "The individual 1 at the beginning"
        )

    def test_individual_middle(self):
        self.assertEqual(
            week5([9, 3, 5, 6, 4, 5, 6, 3, 9]), 4, "The individual 4 at the middle"
        )

    def test_two_individuals(self):
        self.assertEqual(
            week5([9, 3, 5, 6, 4, 5, 6, 3]),
            4,
            "If two individuals will return the smallest one",
        )
