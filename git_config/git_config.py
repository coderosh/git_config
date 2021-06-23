import os
from configparser import ConfigParser


def get_config_path(type="global"):
    home = os.path.expanduser("~")
    cwd = os.getcwd()

    if(type == "local"):
        return os.path.join(cwd, ".git", "config")
    else:
        return os.path.join(home, ".gitconfig")


def get_config(type="global"):
    config = ConfigParser()
    config_path = get_config_path(type)
    config.read(config_path)
    return config._sections
