#!/usr/bin/env python3
"""
Task 3. Tasks

Return asyncio.Task
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random

    Takes an integer and returns a coroutine task.

    Arguments:
        max_delay (int): The maximum delay to be passed to wait_random()

    Return:
        (asyncio.Task): The coroutine task to be executed.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
