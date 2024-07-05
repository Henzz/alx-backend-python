#!/usr/bin/env python3
"""
This module provides a function to create a tuple from a string and a number.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a string and a number.

    Args:
        k (str): The string value.
        v (Union[int, float]): The numeric value.

    Returns:
        Tuple[str, float]: A tuple containing the string `k` and the square of
        `v` as a float.
    """
    return (k, v ** 2)
