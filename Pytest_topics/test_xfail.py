import sys

import pytest


# pytestmark = pytest.mark.xfail


def test_stringjoin():
    s1 = 'Python,Pytest and Automation'
    l1 = ['Python,Pytest', 'and', 'Automation']
    l2 = ['Python', 'Pytest and Automation']
    assert ' '.join(l1) == s1
    # assert ','.join(l2) == s1


# @pytest.mark.xfail(raises=IndexError, reason='No such index')
def test_str04():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    with pytest.raises(IndexError):
        assert letters[100]


@pytest.mark.xfail(sys.platform == 'win32', reason='Run`s only in Linux operating system')
def test_str05():
    letters = 'abcd'
    numbers = 1234
    assert letters + numbers == 'abcd1234'
