#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay
and returns the delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        Waits for a random delay between 0 and max_delay
        seconds and returns the delay.

        Args:
            max_delay (int or float, optional): The maximum
            delay in seconds. Default set to 10.

        Returns:
            float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
