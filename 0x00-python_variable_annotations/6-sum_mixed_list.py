#!/usr/bin/env python3
"""
This module provides a function to sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list of integer and float values.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integer and float values to be summed.

    Returns:
        float: The sum of the values in the input list.
    """
    return sum(mxd_lst)
