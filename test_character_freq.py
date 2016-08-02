import pytest
from character_freq import CharFreq


"""
Code for unit testing character_freq.py
"""


def test_char_freq_with_valid_input():
    """
    Positive Testing
    Valid inputs are provided
    """
    output = {'a': 4, 's': 6, 'd': 5}
    assert CharFreq().char_freq('asddsaassadsdsd') == output


def test_char_freq_with_invalid_input_integer():
    """
    Negative Testing
    Non-iteratable integer input is provided.
    """
    with pytest.raises(Exception):
        assert CharFreq().char_freq(45354565645)
