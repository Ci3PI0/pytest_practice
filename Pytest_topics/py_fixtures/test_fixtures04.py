month = ['Mar', 'Jan', 'Dec']


# def some_func():
#     return 1
#
#
# def some_other_func():
#     return 2


def test_checkrequest(setup04):
    assert 'April' in setup04
    assert len(setup04) == 4
    # assert setup04 == 2
    print(setup04)


def test_fixture_function(setup05):
    print(f'\n{setup05('list')}')
    assert setup05('list') == [1,2,3]
    print(f'\n{setup05('tuple')}')
    assert setup05('tuple') == (1,2,3)