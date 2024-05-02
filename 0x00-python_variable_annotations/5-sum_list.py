#!/usr/bin/env python3
"""
Task 5. Complex types - list of floats

Takes list input of floats, returns sum
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum_list

    Sums list of floats

    Arguments:
        input_list (List[float]): The input list to calculate their sum.

    Return:
        (float): The calculated sum of all the floats in the list.
    """
    return sum(input_list)
