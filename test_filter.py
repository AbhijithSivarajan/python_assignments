import pytest
from filter import Filter, is_valid_choice


"""
Code for unit testing filter.py
"""


def test_filter_long_words_with_valid_inputs():
    """
    Positive Testing
    Valid inputs are provided.
    """

    input_list = ['asd', 'dsa', 'fg']
    output_list = ['asd', 'dsa']
    assert Filter().filter_long_words(2, input_list, 2) == output_list


def test_filter_long_words_with_invalid_maximum_length():
    """
    Negative Testing
    Invalid maximum length is provided.
    """

    input_list = ['asd', 'dsa', 'fg']
    with pytest.raises(Exception):
        assert Filter().filter_long_words(2, input_list, '$')


def test_choice_with_valid_inputs():
    """
    Positive Testing
    Valid choice is provided.
    """

    assert is_valid_choice(1) is True


def test_choice_with_invalid_choice():
    """
    Negative Testing
    Invalid choice is provided(choice not in [1,2])
    """

    assert is_valid_choice(3) is False


def test_choice_with_invalid_inputs_string():
    """
    Negative Testing
    Invalid choice provided(type is string)
    """

    assert is_valid_choice('one') is False
