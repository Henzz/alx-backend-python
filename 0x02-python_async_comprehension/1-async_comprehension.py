#!/usr/bin/env python3
"""
This module contains the async_comprehension coroutine.
"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    A coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [num async for num in async_generator()]
