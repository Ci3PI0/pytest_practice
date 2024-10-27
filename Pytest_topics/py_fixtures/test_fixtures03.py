def test_delItem(setup01, weekdays1):
    del setup01[-1]
    print(setup01)
    assert setup01 == weekdays1


def test_removeItem(setup02, weekdays2):
    print('\n',setup02,sep='')
    setup02.remove('thur')
    assert setup02 == weekdays2
    print(setup02)
