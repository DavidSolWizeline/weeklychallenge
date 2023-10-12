from typing import List, Tuple

"""
Week 1 Code Challenge
Challenge Details:
Problem: Covering Set
Description: Given a set of closed intervals, find the smallest set of numbers that
    covers all the intervals. If there are multiple smallest sets, return any of them.
Input: An array of intervals. Each interval is represented as an array of two numbers
    [a, b], with a <= b.
Output: An array of numbers, representing the set of numbers that covers all the
    intervals.
Deadline: Monday, Oct. 16th EOD
"""


def week1(input: List[Tuple[int, int]]) -> List[int]:
    """
    Will look for the intersections between the intervals in the input list.
    At the end will take the first value of each intersection as the result.
    The rules for the intersections are:
    - If the interval completely includes the intersection, ignore the interval.
    - If the interval is completely inside an intersection, it replaces that
        intersection.
    - If the interval intersects an existing intersection, then the intersection
        replaces the existing intersection.
    - Else will add the interval as a new intersection.
        That is the case of the first intersection.

    Args:
        input (List[Tuple[int, int]]): List of the tuples defining the input intervals.

    Returns:
        List[int]: List of one set of numbers that cover all the intervals.
    """
    # Create a list of integers for the output
    output: List[int] = []
    # Create a list of intersections
    intersections: List[Tuple[int, int]] = []
    # For all the input interval tuples
    for interval in input:
        # Flag the interval as not processed
        processed: bool = False
        # For all existing intersections
        for intersection_index, intersection in enumerate(intersections):
            # If the interval completely includes the intersection, ignore the interval.
            if (interval[0] <= intersection[0]) and (interval[1] >= intersection[1]):
                processed = True
                break
            # If the interval completely inside the intersection
            if (interval[0] >= intersection[0]) and (interval[1] <= intersection[1]):
                intersections[intersection_index] = interval
                processed = True
                break
            # If the interval intersects the intersection, use the intersection as the
            # new intersection.
            # Option one, the interval intersects the start of the interval
            if (
                (interval[0] < intersection[0])
                and (interval[1] < intersection[1])
                and (interval[1] > intersection[0])
            ):
                intersections[intersection_index] = (intersection[0], interval[1])
                processed = True
                break
            # Option two, the interval intersects at the end of the interval
            if (
                (interval[0] > intersection[0])
                and (interval[1] > intersection[1])
                and (interval[0] < intersection[1])
            ):
                intersections[intersection_index] = (interval[0], intersection[1])
                processed = True
                break
        if not processed:
            # If the interval doesn't intersects any of the existing intervals,
            # add it as a new interval
            intersections.append(interval)
    # For each resulting intersection, add the first element to the output
    for intersection in intersections:
        output.append(intersection[0])
    # Sort the output list
    output.sort()
    # Return the result list
    return output
