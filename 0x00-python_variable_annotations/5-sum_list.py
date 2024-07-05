#!/usr/bin/env python3
"""
This module provides a function to sum a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of float values.

    Args:
        input_list (List[float]): The list of float values to be summed.

    Returns:
        float: The sum of the values in the input list.
    """
    return sum(input_list)
