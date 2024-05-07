#!/usr/bin/env python3
"""
Task 1. Async Comprehensions

async_comprehension coroutine.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async_comprehension

    A coroutine that collects the 10 numbers from async_generator and
    returns it.

    Return:
        (List[float]): A list of all the results given by the async_generator
    """
    result = [i async for i in async_generator()]
    return result
