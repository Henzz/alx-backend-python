#!/usr/bin/env python3
"""
This module provides a function to safely get the first element of a sequence.
"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the input sequence, or None if the sequence
    is empty.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence, or None if the
        sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
