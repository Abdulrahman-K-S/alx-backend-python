#!/usr/bin/env python3
"""
Task 6. Complex types - mixed list

Takes list input of of integers and floats, returns float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list
    
    Sums list of of integers and floats
    
    Arguments:
        mxd_lst (List[Union[int, float]]): A mixed list conatining ints
        & floats

    Return:
        (float): The sum of all the numbers inside the mixed list.    
    """
    return sum(mxd_lst)
