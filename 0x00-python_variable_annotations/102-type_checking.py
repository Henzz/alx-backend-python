#!/usr/bin/env python3
"""
This module provides a function to zoom in on a tuple.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zoom in on a tuple by repeating each element a given number of times.

    Args:
        lst (Tuple[int, ...]): The input tuple to be zoomed in.
        factor (int): The number of times to repeat each element. Defaults
        to 2.

    Returns:
        Tuple[int, ...]: The zoomed-in tuple.
    """
    zoomed_in: Tuple[int, ...] = tuple(item for item in lst
                                       for _ in range(factor))
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
print(zoom_2x)  # Output: (12, 12, 72, 72, 91, 91)

zoom_3x = zoom_array(array, 3)
print(zoom_3x)  # Output: (12, 12, 12, 72, 72, 72, 91, 91, 91)
