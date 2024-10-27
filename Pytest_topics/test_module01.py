import pytest


def test_tc_api_auth():
    print('First Test')
    a = 4
    b = 6
    assert a - b == 10


def func1():
    raise ValueError('Exception func1 raised')


def test_tc_api_auth2():
    with pytest.raises(Exception) as exif:
        a = 5
        b = 6
        # assert a + b == 10
        func1()
    print(str(exif))
    assert str(exif.value) == 'Exception func1 raised'
    # assert a + b == 10


def test_tc_api_log_out():
    a = 2
    b = 6
    assert a / b == 12
