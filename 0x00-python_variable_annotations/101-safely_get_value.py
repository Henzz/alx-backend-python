#!/usr/bin/env python3
"""
This module provides a function to safely get a value from a dictionary.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get the value from a dictionary for a given key.

    If the key is found in the dictionary, the value is returned.
    Otherwise, the default value (or None if no default is
    provided) is returned.

    Returns:
        Union[Any, T]: The value from the dictionary, or the
        default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
