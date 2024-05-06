#!/usr/bin/env python3
"""
Task 0. The basics of async

An asynchronous coroutine
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait_random

    An asynchronous coroutine that takes in an integer argument and
    waits for a random delay between 0 and max_delay
    seconds and eventually returns it.

    Arguments:
        max_delay (int): The max delay it could wait for.

    Return:
        (float): The time in seconds it waited.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
