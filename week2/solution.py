"""
Week 2 Code Challenge
Problem: Peculiar Trees
Description: You are given a binary tree in a peculiar string representation.
    Each node is written in the form (lr), where l corresponds to the left child and r
    corresponds to the right child. If either l or r is null, it will be represented as
    a zero. Otherwise, it will be represented by a new (lr) pair.
Input: A string, representing the tree.
Output: A integer, representing the depth of the tree
Deadline: Monday, Oct. 30th EOD
Examples:
    A root node with no children: (00)
    A root node with two children: ((00)(00))
    An unbalanced tree with three consecutive left children: ((((00)0)0)0)
"""


def week2(tree: str) -> int:
    """
    Reads the symbols in the tree representation. Each time a "(" is found, it means there is a node and the depth
    increases by one. Each time a ")" is found, it means the node "ended" and the depth decreases by one. At each step
    we compare the "current" depth to the maximum previously found depth and take the biggest of the two. At the end
    of the tree representation the maximum depth is the expected result.

    Args:
        input (str): String representation of the binary tree.

    Returns:
        int: Maximum depth of the tree
    """
    # Initialize depth and max_depth
    depth: int = 0
    max_depth: int = 0
    # Read the input
    for symbol in tree:
        # If the symbol is a left bracket, increase depth
        if symbol == "(":
            depth += 1
        # If the symbol is a right bracket, decrease depth
        elif symbol == ")":
            depth -= 1
        else:
            # Ignore the symbol
            pass
        # Update the max_depth
        max_depth = max(depth, max_depth)
    # Return the max_depth
    return max_depth
