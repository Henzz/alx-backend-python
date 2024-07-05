#!/usr/bin/env python3
"""
This module provides a function to get the length of each element in a list.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element from the
    input list and the length of that element.

    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where the first element
        of each tuple is a sequence from the input list, and the second element
        is the length of that sequence.
    """
    return [(i, len(i)) for i in lst]
