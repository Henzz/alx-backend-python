#!/usr/bin/env python3

"""
Unit tests for the utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized

from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
"""
Test suite for the utils.access_nested_map function.
"""

json

Copy
@parameterized.expand([
    ({"a": 1}, ("a",), 1),
    ({"a": {"b": 2}}, ("a",), {"b": 2}),
    ({"a": {"b": 2}}, ("a", "b"), 2),
])
def test_access_nested_map(self, nested_map: dict, path: tuple, expected: any) -> None:
    """
    Test that the utils.access_nested_map function returns the expected value.

    Args:
        nested_map (dict): The nested map to access.
        path (tuple): The path to the desired value.
        expected (any): The expected value to be returned.
    """
    self.assertEqual(access_nested_map(nested_map, path), expected)


if name == 'main':
    unittest.main()