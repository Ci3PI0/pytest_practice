from Pytest_topics.utils.ConfigFileParser import ConfigFileParser

config = ConfigFileParser('prod.ini')

def test_prod_config():
    print(config.getSectionParam('fl_1','iin'))