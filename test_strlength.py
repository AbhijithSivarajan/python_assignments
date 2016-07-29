from strlength import Length, is_valid_choice
import pytest


"""
For testing built_in() method
"""


def test_built_in_with_valid_input_string():
    """
    For testing built_in() method.
    Positive Testing
    """
    assert Length().built_in('abhi') == 4


def test_built_in_with_valid_input_list():
    """
    For testing built_in() method.
    Positive Testing
    """
    assert Length().built_in(['asd', 'dsa']) == 2


def test_built_in_with_invalid_input():
    """
    For testing built_in() method.
    Negative Testing
    """
    with pytest.raises(Exception) as e:
        assert Length().built_in(1)

"""
For testing without_built_in() method
"""


def test_without_built_in_with_valid_input_string():
    """
    For testing without_built_in() method.
    Positive Testing
    """
    assert Length().without_built_in('abhi') == 4


def test_without_built_in_with_valid_input_list():
    """
    For testing without_built_in() method.
    Positive Testing
    """
    assert Length().without_built_in(['asd', 'dsa']) == 2


def test_without_built_in_with_invalid_input():
    """
    For testing without_built_in() method.
    Negative Testing
    """
    with pytest.raises(Exception) as e:
        assert Length().without_built_in(1)


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
