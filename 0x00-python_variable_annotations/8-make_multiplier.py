#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of the float and the multiplier.
    """
    def multiplier_function(num: float) -> float:
        """
        Multiplies a float by the given multiplier.

        Args:
            num (float): The value to be multiplied.

        Returns:
            float: The result of multiplying the given number by the
            multiplier.
        """
        return num * multiplier
    return multiplier_function
