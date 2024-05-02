#!/usr/bin/env python3
"""
Task 8. Complex types - functions

Takes a float multiplier,
returns a function that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier

    Takes a float and returns a float

    Arguments:
        multiplier (float): The multiplier to multiply in the function

    Return:
        (Callable[[float], float]): A function that multiplies the float
        by the multipler
    """
    return (lambda x: multiplier*x)
