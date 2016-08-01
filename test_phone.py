from phone import Phone
import pytest


"""
Code for unit testing phone.py
"""


def test_is_valid_phone_number_with_hyphen():
    """
    Positive Testing
    Valid phone number given separated by hyphen(-).
    """
    phone = '416-789-5308'
    result = Phone().parse_phone_number(phone)
    assert result.get('area_code') == '416'
    assert result.get('trunk') == '789'
    assert result.get('phone_number') == '5308'


def test_is_valid_phone_number_with_space():
    """
    Positive Testing
    Valid phone number given separated by space.
    """
    phone = '416 789 5308'
    result = Phone().parse_phone_number(phone)
    assert result.get('area_code') == '416'
    assert result.get('trunk') == '789'
    assert result.get('phone_number') == '5308'


def test_is_valid_phone_number_with_dot():
    """
    Positive Testing
    Valid phone number given separated by dot(.)
    """
    phone = '416.789.5308'
    result = Phone().parse_phone_number(phone)
    assert result.get('area_code') == '416'
    assert result.get('trunk') == '789'
    assert result.get('phone_number') == '5308'


def test_is_valid_phone_number_with_round_brackets_on_area_code():
    """
    Positive Testing
    Valid phone number given with round brackets on area code.
    """
    phone = '(416) 789-5308'
    result = Phone().parse_phone_number(phone)
    assert result.get('area_code') == '416'
    assert result.get('trunk') == '789'
    assert result.get('phone_number') == '5308'


def test_is_valid_phone_number_starting_with_1_and_hyphen():
    """
    Positive Testing
    Valid phone number given separated by hyphen(-) starting with '1-'.
    """
    phone = '1-416-789-5308'
    result = Phone().parse_phone_number(phone)
    assert result.get('area_code') == '416'
    assert result.get('trunk') == '789'
    assert result.get('phone_number') == '5308'


def test_is_valid_phone_number_with_extension_with_hyphen():
    """
    Positive Testing
    Valid phone number with extension given separated by hyphen(-).
    """
    phone = '416-789-5308-1111'
    result = Phone().parse_phone_number(phone)
    assert result.get('area_code') == '416'
    assert result.get('trunk') == '789'
    assert result.get('phone_number') == '5308'
    assert result.get('extension') == '1111'


def test_is_valid_phone_number_with_extension_specified_by_x():
    """
    Positive Testing
    Valid phone number with extension specified by x.
    """
    phone = '416-789-5308x1111'
    result = Phone().parse_phone_number(phone)
    assert result.get('area_code') == '416'
    assert result.get('trunk') == '789'
    assert result.get('phone_number') == '5308'
    assert result.get('extension') == '1111'


def test_is_valid_phone_number_with_extension_specified_by_ext():
    """
    Positive Testing
    Valid phone number with extension specified by ext.
    """
    phone = '416-789-5308 ext. 1111'
    result = Phone().parse_phone_number(phone)
    assert result.get('area_code') == '416'
    assert result.get('trunk') == '789'
    assert result.get('phone_number') == '5308'
    assert result.get('extension') == '1111'


def test_is_valid_phone_number_with_extension_specified_by_hash():
    """
    Positive Testing
    Valid phone number with extension specified by #.
    """
    phone = 'emergency 1-(416) 789.5308 #1111'
    result = Phone().parse_phone_number(phone)
    assert result.get('area_code') == '416'
    assert result.get('trunk') == '789'
    assert result.get('phone_number') == '5308'
    assert result.get('extension') == '1111'


def test_is_valid_phone_number_with_invalid_area_code():
    """
    Negative Testing
    Invalid phone number with invalid area code(len(area_code) != 3).
    """
    phone = '1234-897-2105'
    with pytest.raises(Exception):
        assert Phone().parse_phone_number(phone)


def test_is_valid_phone_number_with_invalid_trunk():
    """
    Negative Testing
    Invalid phone number with invalid trunk(len(trunk) != 3).
    """
    phone = '416-1234-3597'
    with pytest.raises(Exception):
        assert Phone().parse_phone_number(phone)


def test_is_valid_phone_number_with_invalid_phone_number():
    """
    Negative Testing
    Invalid phone number with invalid phone number(len(phone_number) != 4).
    """
    phone = '416-789-65423'
    with pytest.raises(Exception):
        assert Phone().parse_phone_number(phone)


def test_is_valid_phone_number_with_invalid_extension():
    """
    Negative Testing
    Invalid phone number with invalid extension(len(extension) != 4).
    """
    phone = '416-789-2354-112233'
    with pytest.raises(Exception):
        assert Phone().parse_phone_number(phone)


def test_is_valid_phone_number_with_invalid_separator():
    """
    Negative Testing
    Invalid phone number with invalid separator.
    """
    phone = '416/789/2354'
    with pytest.raises(Exception):
        assert Phone().parse_phone_number(phone)
