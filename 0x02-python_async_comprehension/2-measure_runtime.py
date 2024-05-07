#!/usr/bin/env python3
"""
Task 2. Run time for four parallel comprehensions

measure_runtime coroutine.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime

    Measures the total runtime of async_comprehension and returns it.

    Return:
        (float): The total wait time.
    """
    startingTime = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    endingTime = time.perf_counter()
    return endingTime - startingTime
