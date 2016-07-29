from filter import Filter, is_valid_choice
import pytest


"""
For testing filter_long_words() method
"""


def test_filter_long_words_with_valid_inputs():
    """
    For testing filter_long_words() method.
    Positive Testing
    """

    input_list = ['asd', 'dsa', 'fg']
    output_list = ['asd', 'dsa']
    assert Filter().filter_long_words(2, input_list, 2) == output_list


def test_filter_long_words_with_invalid_inputs():
    """
    For testing filter_long_words() method.
    Negative Testing
    """

    input_list = ['asd', 'dsa', 'fg']
    with pytest.raises(Exception):
        assert Filter().filter_long_words(2, input_list, '$')


def test_filter_long_words_with_invalid_inputs_1():
    """
    For testing filter_long_words() method.
    Negative Testing
    """

    input_list = ['asd', 'dsa', 'fg']
    with pytest.raises(Exception):
        assert Filter().filter_long_words('$', input_list, 2)


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
