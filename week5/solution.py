"""
Week 5 Code Challenge
Problem: Lonely Integer
Description: Given an array of integers, where all elements but one occur twice, find the unique element.
Input: An array of integers a, It’s guaranteed that a has and odd number of elements and there's only one unique element
Output: An integer
Deadline: Monday, Dec. 11 EOD
Examples:
    A root node with no children: (00)
    A root node with two children: ((00)(00))
    An unbalanced tree with three consecutive left children: ((((00)0)0)0)
"""


from typing import Optional


def week5(integers_list: list[int]) -> int:
    """
    Finds the lone integer in the list. The list must have an odd number of integers,
    every integer has a pair except for one.

    Args:
        integers_list (list[int]): The list of integers.

    Returns:
        int: The lone integer.
    """
    # Sorts the list, don't really care to do a quick_sort "by hand" :P
    integers_list.sort()
    # Previous value, to discard pairs
    previous_value: Optional[int] = None
    # Iterate through the list until you find the lone integer
    for integer in integers_list:
        # If it is the first of the pair (or the individual integer) store it
        if not previous_value:
            previous_value = integer
        else:
            # If its the pair, set previous_value to None
            if integer == previous_value:
                previous_value = None
            # If it is not, then this is the individual integer
            else:
                return previous_value
    # If the individual is the biggest number, return it
    if previous_value:
        return previous_value
    # If the individual integer was not found, returns -1
    return -1
