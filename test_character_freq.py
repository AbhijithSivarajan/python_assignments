from character_freq import CharFreq
import pytest


"""
Code for unit testing character_freq.py
"""


def test_char_freq_with_valid_input():
    """
    For testing char_freq() method.
    Positive Testing
    """

    output = {'a': 4, 's': 6, 'd': 5}
    assert CharFreq().char_freq('asddsaassadsdsd') == output


def test_char_freq_with_invalid_input_integer():
    """
    For testing char_freq() method.
    Negative Testing
    """

    with pytest.raises(Exception):
        assert CharFreq().char_freq(45354565645)
