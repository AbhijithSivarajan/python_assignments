from overlap import overlapping
import pytest


"""
Code for unit testing overlapping.py
"""


def test_overlapping_with_valid_inputs():
    """
    For testing overlapping() method.
    Positive Testing
    """

    list1 = ['asd', 'as', 'aef']
    list2 = ['dsa', 'sdv', 'eqweqw', 'asd']
    assert overlapping(list1, list2) is True


def test_overlapping_with_invalid_inputs_not_list():
    """
    For testing overlapping() method.
    Negative Testing
    """

    list1 = ['asd', 'as', 'aef']
    with pytest.raises(Exception):
        assert overlapping(list1, 123)
