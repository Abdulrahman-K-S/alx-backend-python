#!/usr/bin/env python3
"""
Task 7. Complex types - string and int/float to tuple

Takes a string k and an int OR float, returns a tuple
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv

    Takes a string and int/float and returns a tuple.

    Arguments:
        k (str): The key variable which is a string.
        v (Union[int, float]): The value variable which could be a string
        or float

    Return:
        (Tuple[str, float]): A tuple of both key & value. Value will always
        be a float regardless if it's a int or not.
    """
    return (k, v ** 2)
