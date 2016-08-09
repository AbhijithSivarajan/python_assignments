import pytest
from encode_decode import Coder, is_valid_choice


"""
Code for unit testing encode_decode.py
"""


def test_encode_with_valid_inputs():
    """
    Positive Testing
    Providing valid inputs
    """
    assert Coder('defg', 3).encode() == 'abcd'


def test_encode_with_invalid_number_of_shifts():
    """
    Negative Testing
    Providing invalid input for number_of_shifts.
    """
    with pytest.raises(Exception):
        assert Coder('defg', '$').encode()


def test_decode_with_invalid_number_of_shifts():
    """
    Negative Testing
    Providing invalid type for number_of_shifts.
    """
    y = "Gb or be abg gb or, Gung vf gur dhrfgvba."
    with pytest.raises(Exception):
        assert Coder(y, 'one').decode()


def test_decode_with_valid_inputs():
    """
    Positive Testing
    Providing valid inputs
    """
    assert Coder("Nkrru!!!", 46).decode() == "Hello!!!"


def test_choice_with_valid_inputs():
    """
    Positive Testing
    Providing valid choice
    """
    assert is_valid_choice(1) is True


def test_choice_with_invalid_choice():
    """
    Negative Testing
    Providing invalid choice
    """
    assert is_valid_choice(3) is False


def test_choice_with_invalid_inputs_string():
    """
    Negative Testing
    Providing invalid type for choice.
    """
    assert is_valid_choice('one') is False
