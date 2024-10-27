import pytest


@pytest.fixture()
def setup_list():
    print('\n in fixture \n')
    city = ['New York', 'Almaty', 'London', 'Astana']
    return city


def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == ['New York', 'London']


def myReverse(lst):
    lst.reverse()
    return lst


def test_reverseList(setup_list):
    assert setup_list[::-2] == ['Astana', 'Almaty']


def test_reverseAllList(setup_list):
    assert setup_list[::-1] == myReverse(setup_list)

@pytest.mark.xfail(reason='Fixture not working')
@pytest.mark.usefixtures("setup_list")
def test_usefixturedemo():
    print(setup_list[0])
    assert 1==1

