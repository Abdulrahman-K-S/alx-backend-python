#!/usr/bin/env python3
"""
Task 0. Async Generator

async_generator coroutine.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """async_generator

    A coroutine that loops 10 times and each time it waits 1 second
    and then yeild a number from 1 to 10.

    Return:
        (AsyncGenerator[float, None]): A float generated from an async
        coroutine.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random * 10
