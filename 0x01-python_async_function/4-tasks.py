#!/usr/bin/env python3
"""
This module calls task_wait_random.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates n tasks with task_wait_random(max_delay) and waits
    for them all to complete.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay in seconds.

    Returns:
        list[float]: The list of delays (in seconds) for each completed task.
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
