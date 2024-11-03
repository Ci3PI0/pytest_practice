import configparser
from pathlib import Path


cfgFile = 'qa.ini'
cfgFileDirectory = 'config'

BASE_DIR = Path(__file__).parent.parent
CONFIG_FILE =BASE_DIR.joinpath(cfgFileDirectory).joinpath(cfgFile)

config = configparser.ConfigParser()
config.read(CONFIG_FILE)


def getSectionParam(section, param):
    return config[section][param]

print(getSectionParam('gmail','pass'))