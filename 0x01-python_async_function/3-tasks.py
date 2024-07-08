#!/usr/bin/env python3
"""
This module returns a asyncio.Task
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random(max_delay) coroutine.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The created Task.
    """
    return asyncio.create_task(wait_random(max_delay))
