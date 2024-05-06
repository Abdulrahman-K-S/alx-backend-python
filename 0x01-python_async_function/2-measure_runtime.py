#!/usr/bin/env python3
"""
Task 2. Measure the runtime

Cacluates the total time taken for all calls to finish
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measure_time

    This function calculates the total time the wait_n() took to
    execute all its calls of wait_random().

    Arguments:
        n (int): The number of wait_random to spawn.
        max_delay (int): The maximum delay to pass to each wait_random call.

    Return:
        (float): The total time the wait_n function took to execute.
    """
    startingTime = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    totalTime = time.perf_counter() - startingTime
    return totalTime / n
