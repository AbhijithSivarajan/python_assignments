from encode_decode import Coder, is_valid_choice
import pytest


"""
Code for unit testing encode_decode.py
"""


def test_encode_with_valid_inputs():
    """
    For testing encode() method.
    Positive Testing
    """
    assert Coder('defg', 3).encode() == 'abcd'


def test_encode_with_invalid_number_of_shifts():
    """
    For testing encode() method.
    Negative Testing
    Providing invalid number_of_switch
    """
    with pytest.raises(Exception):
        assert Coder('defg', '$').encode()


"""
For testing decode() method
"""


def test_decode_with_invalid_number_of_shifts():
    """
    For testing decode() method.
    Negative Testing
    Providing invalid number_of_switch
    """
    y = "Gb or be abg gb or, Gung vf gur dhrfgvba."
    with pytest.raises(Exception):
        assert Coder(y, 'one').decode()


def test_decode_with_valid_inputs():
    """
    For testing decode() method.
    Positive Testing
    """
    assert Coder("Nkrru!!!", 46).decode() == "Hello!!!"


"""
For testing is_valid_choice() method
"""


def test_choice_with_valid_inputs():
    """
    For testing is_valid_choice() method.
    Positive Testing
    """
    assert is_valid_choice(1) is True


def test_choice_with_invalid_choice():
    """
    For testing is_valid_choice() method.
    Negative Testing
    """
    assert is_valid_choice(3) is False


def test_choice_with_invalid_inputs_string():
    """
    For testing is_valid_choice() method.
    Negative Testing
    """
    assert is_valid_choice('one') is False
