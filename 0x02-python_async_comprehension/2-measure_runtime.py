#!/usr/bin/env python3
"""
This module contains the measure_runtime coroutine.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A coroutine that executes async_comprehension four times in parallel
    using asyncio.gather, and measures the total runtime.
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()
    return end_time - start_time
