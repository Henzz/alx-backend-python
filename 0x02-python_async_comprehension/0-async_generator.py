#!/usr/bin/env python3
"""
This module runs time asynchronous 10 times and yield
a random number between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times asycnhronously waiting 1 second between
    then yields a random number 0-10.

    Yields:
        random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
