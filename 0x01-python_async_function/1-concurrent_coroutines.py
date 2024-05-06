#!/usr/bin/env python3
"""
Task 1. Let's execute multiple coroutines at the same time with async

Spawning n numbers of wait_random
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n

    wait_n spawns `n` numbers of the wait_random function passing in
    the max_delay to each spawned function creating a varity of
    wait times.

    Arguments:
        n (int): The number of times to call the wait_random function.
        max_delay (int): The max delay to pass to the function.

    Return:
        (List[float]): A list of the all waited times.
    """
    delays = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delay_list = [await delay for delay in asyncio.as_completed(delays)]
    return delay_list
