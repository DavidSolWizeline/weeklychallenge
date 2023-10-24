""" Create tests for the week2 function in week2/solution.py file"""
import unittest

from week2.solution import week2


class TestWeek2(unittest.TestCase):
    """Test class for week2.py"""

    def test_no_interval(self):
        self.assertEqual(week2(""), 0, "If no tree max_depth = 0")

    def test_only_root_node(self):
        self.assertEqual(week2("(00)"), 1, "If only the root node max_depth = 1")

    def test_only_one_child_left(self):
        self.assertEqual(
            week2("((00)0)"),
            2,
            "Only one child to the left, max_depth = 2",
        )

    def test_only_one_child_right(self):
        self.assertEqual(
            week2("(0(00))"),
            2,
            "Only one child to the right, max_depth = 2",
        )

    def test_my_example(self):
        self.assertEqual(
            week2("((00)((00)0))"),
            3,
            "Example in the readme, max_depth = 3",
        )

    def test_unbalanced_tree(self):
        self.assertEqual(
            week2("((((00)0)0)0)"),
            4,
            "An unbalanced tree with three consecutive left children, max_depth = 4",
        )
