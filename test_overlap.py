import pytest
from overlap import overlapping, access_input


"""
Code for unit testing overlapping.py
"""


def test_overlapping_with_valid_inputs():
    """
    Positive Testing
    Valid inputs are provided
    """

    list1 = ['asd', 'as', 'aef']
    list2 = ['dsa', 'sdv', 'eqweqw', 'asd']
    assert overlapping(list1, list2) is True


def test_overlapping_with_invalid_inputs_not_list():
    """
    Negative Testing
    List inputs are not provided
    """

    list1 = ['asd', 'as', 'aef']
    with pytest.raises(Exception):
        assert overlapping(list1, 123)
