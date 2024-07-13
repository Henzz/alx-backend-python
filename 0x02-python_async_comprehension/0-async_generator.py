#!/usr/bin/env python3
"""
This module runs time asynchronous 10 times and yield
a random number between 0 and 10.
"""

import asyncio
import random


async def async_generator() -> int:
    """
    Loops 10 times asycnhronously waiting 1 second between
    then yields a random number 0-10.

    Return:
        random number between 0 and 10
    """
    async for i in 10:
        yield i
        await asyncio.sleep(1)
