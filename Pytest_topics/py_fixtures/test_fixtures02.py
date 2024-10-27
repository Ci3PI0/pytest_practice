import pytest

weekdays1 = ['mon', 'tue', 'wed']
weekdays2 = ['fri', 'sat', 'sun']


@pytest.fixture()
def setup01():
    wk1 = weekdays1.copy()
    wk1.append('thur')
    yield wk1
    print(wk1)
    wk1.pop(1)
    print(wk1)
    wk1.clear()
    print(wk1)
    print("\n After yield in setup01 fixture")


@pytest.fixture()
def setup02():
    wk2 = weekdays2.copy()
    wk2.insert(0, 'thur')
    yield wk2
    print(wk2)
    print("\n After yield in setup02 fixture")


def test_extendList(setup01):
    setup01.extend(weekdays2)
    assert setup01 == ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']


def test_len(setup01, setup02):
    assert len(weekdays1 + setup02) == len(setup01 + weekdays2)
