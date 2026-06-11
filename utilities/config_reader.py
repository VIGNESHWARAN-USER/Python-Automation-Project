from configparser import ConfigParser


def get_value(filepath,category, key):
    config = ConfigParser()
    config.read(filepath)
    return config.get(category, key)