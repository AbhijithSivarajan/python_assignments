from url import is_valid_url
import pytest


"""
Code for unit testing url.py
"""


def test_url_with_valid_url_with_http():
    """
    Positive Testing
    Valid url given with http protocol.
    """
    url = 'http://slack.emtecinc.com:9090/v0.2/api/messages'
    assert is_valid_url(url) is True


def test_url_with_valid_url_with_ftp():
    """
    Positive Testing
    Valid url given with ftp protocol.
    """
    url = 'ftp://sap.emtecinc.com:8080/v0.2/api/groups'
    assert is_valid_url(url) is True


def test_url_with_valid_url_without_port_number():
    """
    Positive Testing
    Valid url given without port number.
    """
    url = 'https://empower.emtecinc.com/v0.2/api/robos'
    assert is_valid_url(url) is True


def test_url_with_valid_url_with_specified_symbols_in_the_end():
    """
    Positive Testing
    Valid url given with specified symbols in the end.
    """
    url = 'https://empower.emtecinc.com/v0.2/api/robos_AS-12.3'
    assert is_valid_url(url) is True


def test_url_with_invalid_url_without_port_number():
    """
    Negative Testing
    Specifying colon(:) without port number.
    """
    url = 'https://empower.emtecinc.com:/v0.2/api/robos'
    assert is_valid_url(url) is False


def test_url_with_invalid_version_number():
    """
    Negative Testing
    Specifying version number with more than two-digit version.
    """
    url = 'https://empower.emtecinc.com:8008/v13.4/api/robos'
    assert is_valid_url(url) is False


def test_url_with_invalid_protocol():
    """
    Negative Testing
    Providing invalid protocol.
    """
    url = 'htps://empower.emtecinc.com:8008/v1.4/api/robos'
    assert is_valid_url(url) is False


def test_url_with_invalid_host_name():
    """
    Negative Testing
    Providing invalid host name.
    """
    url = 'https://empower.google.com:8008/v1.4/api/robos'
    assert is_valid_url(url) is False


def test_url_with_invalid_port_number():
    """
    Negative Testing
    Providing invalid port number(len(port_number) != 4).
    """
    url = 'https://empower.emtecinc.com:80080230/v3.4/api/robos'
    assert is_valid_url(url) is False


def test_url_with_invalid_symbols_in_the_end():
    """
    Negative Testing
    Providing invalid symbols in the end.
    """
    url = 'https://empower.emtecinc.com:8008/v1.4/api/robos/trial#'
    assert is_valid_url(url) is False
