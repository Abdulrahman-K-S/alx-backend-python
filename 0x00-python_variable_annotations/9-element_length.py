#!/usr/bin/env python3
"""
Task 9. Let's duck type an iterable object

Annotates the below function's parameters
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length
    
    .
    .
    .
    """
    return [(i, len(i)) for i in lst]
