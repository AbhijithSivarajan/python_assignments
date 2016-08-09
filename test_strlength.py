import pytest
from strlength import Length, is_valid_choice


def test_built_in_with_valid_input_string():
    """
    Positive Testing
    Providing valid input string
    """
    assert Length().built_in('abhi') == 4


def test_built_in_with_valid_input_list():
    """
    Positive Testing
    Providing valid input list
    """
    assert Length().built_in(['asd', 'dsa']) == 2


def test_built_in_with_invalid_input():
    """
    Negative Testing
    Providing invalid input(integer)
    """
    with pytest.raises(Exception) as e:
        assert Length().built_in(1)


def test_without_built_in_with_valid_input_string():
    """
    Positive Testing
    Providing valid input string
    """
    assert Length().without_built_in('abhi') == 4


def test_without_built_in_with_valid_input_list():
    """
    Positive Testing
    Providing valid input list
    """
    assert Length().without_built_in(['asd', 'dsa']) == 2


def test_without_built_in_with_invalid_input():
    """
    Negative Testing
    Providing invalid input(integer)
    """
    with pytest.raises(Exception) as e:
        assert Length().without_built_in(1)


def test_choice_with_valid_inputs():
    """
    Positive Testing
    Providing valid choice
    """
    assert is_valid_choice(1) is True


def test_choice_with_invalid_choice():
    """
    Negative Testing
    Providing invalid choice.
    """
    assert is_valid_choice(3) is False


def test_choice_with_invalid_inputs_string():
    """
    Negative Testing
    Providing invalid type for choice.
    """
    assert is_valid_choice('one') is False
