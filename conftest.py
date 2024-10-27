import pytest


@pytest.fixture(scope='module')
def weekdays1():
    return ['mon', 'tue', 'wed']


@pytest.fixture(scope='module')
def weekdays2():
    return ['fri', 'sat', 'sun']


@pytest.fixture(scope='module')
def setup01(weekdays1):
    print('\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    wk1 = weekdays1.copy()
    wk1.append('thur')
    yield wk1
    print('\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    print('\nFixture setup01 closing')
    # Если нужно, можно добавить логику очистки wk1, но не weekdays1
    # Например:
    # wk1.remove('thur')  # Убираем элемент, добавленный в тесте
    print('setup01 final state:', wk1)


@pytest.fixture(scope='module')
def setup02(weekdays2):
    wk2 = weekdays2.copy()
    wk2.insert(0, 'thur')
    yield wk2


@pytest.fixture()
def setup04(request):
    # В данном случае request это корень файла где была вызвана/использована фикстура
    mon = getattr(request.module, 'month').copy()
    mon.append('April')
    # num = getattr(request.module,'some_other_func')
    print('\n in Fixture04 setup')
    print('\n Fixture Scope:' + str(request.scope))
    print('\n Calling function:' + str(request.function.__name__))
    print('\n Calling module:' + str(request.module.__name__))
    yield mon
    # yield num()

@pytest.fixture()
def setup05():
    def get_structure(name):
        if name == 'list':
            return [1,2,3]
        elif name == 'tuple':
            return (1,2,3)
    return get_structure