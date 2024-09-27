#!/usr/bin/env python3
'''
This module provides a function to zoom in on elements of a list by a factor.
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on the elements of the list by repeating them according to
    the factor.

    Returns:
        List: A new list with elements repeated according to the factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
