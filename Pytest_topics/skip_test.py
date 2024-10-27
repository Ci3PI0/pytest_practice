import sys
import pytest

const = 9 / 5
pytestmark = pytest.mark.skipif('win32' != sys.platform, reason=f'Tests runs only on Windows')


def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah


print(cent_to_fah())
a = 5


# @pytest.mark.skipif(sys.version_info.major == 3, reason=f'Major version of Python is {sys.version_info.major}')
def test_case01():
    with pytest.raises(Exception) as exp:
        assert type(const) is int

    print('Type is', str(exp.type), 'Value is ', str(exp.value))


@pytest.mark.skip(reason='i wish that')
def test_case02():
    assert cent_to_fah() == 32


@pytest.mark.skipif(pytest.__version__ == '8.3.3', reason='Tests run only on pytest higher than 8.3.3')
def test_case03():
    print(f'Pytest version {pytest.__version__}')
    assert cent_to_fah(35) == 95.0
