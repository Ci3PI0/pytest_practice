import os.path

import pytest

QA_config = 'qa.prop'
prod_config = 'prod.prop'


def pytest_addoption(parser):
    parser.addoption("--cmdopt", default="QA")


@pytest.fixture
def cmd_opt(pytestconfig):
    print(f'In CmdOpt fixture function')
    opt = pytestconfig.getoption("cmdopt")
    if opt == 'Prod':
        ## os.path.join совмещяет и форматирует путь к файлу
        ## os.path.dirname(__file__)  Путь к текущему файлу
        f = open(os.path.join(os.path.dirname(__file__),prod_config), 'r')
    else:
        f = open(os.path.join(os.path.dirname(__file__),QA_config), 'r')
    yield f