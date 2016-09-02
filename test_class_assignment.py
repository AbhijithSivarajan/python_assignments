import pytest

from connection import Connection
from device_manager import DeviceManager
from notification import NotificationManager
from user import User, UserManager, Authentication


connection = Connection()
cursor = connection.get_cursor()


"""
Code for unit testing User.py
"""


def test_user_valid_with_valid_user_data():
    """
    Positive Testing
    Providing valid user data input.
    """
    user_obj = User(9, 'Abhijith', 317)
    assert Authentication(cursor).is_user_valid(user_obj) is True


def test_user_valid_with_invalid_user_data():
    """
    Negative Testing
    Providing invalid user data input.
    """
    user_obj = User(123, 'Abhijith', 12)
    assert Authentication(cursor).is_user_valid(user_obj) is False


def test_valid_password_with_correct_password():
    """
    Positive Testing
    Providing valid password.
    """
    assert Authentication()._is_valid_password('zillow') is True


def test_valid_password_with_wrong_password():
    """
    Negative Testing
    Providing invalid password.
    """
    assert Authentication()._is_valid_password('emtec') is False


def test_get_user_by_id_with_valid_user_id():
    """
    Positive Testing
    Providing valid user-id input.
    """
    assert UserManager(connection).get_user_by_id(3) is not None


def test_get_user_by_id_with_invalid_user_id():
    """
    Negative Testing
    Providing invalid user-id input.
    """
    with pytest.raises(Exception):
        assert UserManager(connection).get_user_by_id(123)


"""
Code for unit testing DeviceManager.py
"""


def test_if_device_is_available_with_valid_device_model():
    """
    Positive Testing
    Providing valid available device input.
    """
    assert DeviceManager(connection)._is_device_available(
                                     'iPad Air') is not None


def test_if_device_is_unavailable_with_valid_device_model():
    """
    Negative Testing
    Providing valid unavailable device input.
    """
    assert DeviceManager(connection)._is_device_available('iPad') is None


def test_if_device_is_available_with_invalid_device_model():
    """
    Negative Testing
    Providing invalid device input.
    """
    with pytest.raises(Exception):
        assert DeviceManager(connection)._is_device_available('xyz')


def test_request_device_with_available_and_free_device_input():
    """
    Positive Testing
    Providing valid & freely available device input.
    """
    user_obj = User(9, 'Abhijith', 317)
    assert DeviceManager(connection).request_device(
            user_obj, 'iPad Air', 30) is True


def test_request_device_with_available_but_busy_device_input():
    """
    Positive Testing
    Providing valid but currently busy device input.
    """
    user_obj = User(9, 'Abhijith', 317)
    assert DeviceManager(connection).request_device(
            user_obj, 'iPad', 30) is False


def test_request_device_with_unavailable_device_input():
    """
    Negative Testing
    Providing invalid(not available) device input.
    """
    user_obj = User(9, 'Abhijith', 317)
    with pytest.raises(Exception):
        assert DeviceManager(connection).request_device(user_obj, 'xyz', 30)


def test_if_device_is_allocated_with_valid_inputs():
    """
    Positive Testing
    Providing valid allocated device input.
    """
    assert DeviceManager(connection)._is_device_allocated(9, 6) is True


def test_if_device_is_allocated_with_invalid_inputs():
    """
    Positive Testing
    Providing valid allocated device input.
    """
    assert DeviceManager(connection)._is_device_allocated(9, 15) is False


def test_release_device_with_valid_inputs():
    """
    Positive Testing
    Providing valid & allocated device input.
    """
    assert DeviceManager(connection).release_device(9, 6) is True


def test_release_device_with_unallocated_device_inputs():
    """
    Negative Testing
    Providing valid but unallocated device input.
    """
    assert DeviceManager(connection).release_device(9, 16) is None


def test_release_device_with_unallocated_user_inputs():
    """
    Negative Testing
    Providing valid device input but to unallocated user.
    """
    assert DeviceManager(connection).release_device(19, 6) is None


def test_get_device_model_with_valid_device_id():
    """
    Positive Testing
    Providing valid device-id.
    """
    assert DeviceManager(connection)._get_device_model(1) == 'iPhone 5'


def test_get_device_model_with_invalid_device_id():
    """
    Negative Testing
    Providing invalid device-id.
    """
    assert DeviceManager(connection)._get_device_model(0) is None
