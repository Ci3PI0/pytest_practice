import pytest
from pytest_bdd import scenario, scenarios,given,when,then
from pathlib import Path


featureFileDir = 'myfeatures'
featureFile = 'first101.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


def pytest_configure():
    pytest.AMT = 0

@scenario(FEATURE_FILE,'Withdrawal of money')
def test_withdrawal():
    print('End')
    pass

@given('the account balance is 100')
def current_balance():
    pytest.AMT = 100

@when('the account holder withdraws 30')
def withdrawal_amount():
    pytest.AMT = pytest.AMT - 30

@then('the account balance should be 70')
def final_balance():
    assert pytest.AMT == 70