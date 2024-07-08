#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine that awaits for a random
delay between 0 and max_delay seconds and returns the delay.
"""

import asyncio
import random
#from typing import Optional, Union


#async def wait_random(max_delay: Optional[Union[int, float]] = 10) -> float:
async def wait_random(max_delay = 10):
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
