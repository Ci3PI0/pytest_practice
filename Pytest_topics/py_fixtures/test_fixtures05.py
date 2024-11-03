# Parameterization with fixtures
import pytest

@pytest.fixture(params=[(3,4), [3,5]], ids=['tuple', 'list'])
def fixture01(request):
    return request.param

@pytest.fixture(params=['access','slice','assign','len'])
def fixture02(request):
    return request.param


def test_fixture_params01(fixture01):
    print(f'{(type(fixture01))}')
    assert (type(fixture01)) in [tuple, list]
    # assert fixture01 == [3,5]
    assert fixture01 == (3,4)


# @pytest.mark.order(2)
@pytest.mark.parametrize('_str',[1,2,3,4,5,6,True,'false'])
def test_num_data_type(_str):
    print(_str)
    assert type(_str) == int

# @pytest.mark.xfail()
# @pytest.mark.order(1)
def test_fix_param02(fixture01,fixture02):
    if fixture02 == 'access':
        # print(fixture01[2])
        # with pytest.raises(IndexError):
        print(fixture01[0])
        assert fixture01[0]
    elif fixture02 == 'slice':
        print(f'\nSlice part is {fixture01[::-1]}')
        assert fixture01[::-1]
    elif fixture02 == 'assign':
        fixture01[0] = 99
        assert True
    elif fixture02 == 'len':
        print(len(fixture01))
        assert len(fixture01)
