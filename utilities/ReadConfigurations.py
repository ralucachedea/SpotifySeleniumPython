from configparser import ConfigParser
from unicodedata import category


def read_configuration(category, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)