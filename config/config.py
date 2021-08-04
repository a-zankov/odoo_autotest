import configparser
from pathlib import Path
import os


BASE_PATH = Path().absolute()


def create_config(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info",
               "You are using %(font)s at %(font_size)s pt")

    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    """
    Returns the config object
    """
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, setting):
    """
    Print out a setting
    """
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )

    print(msg)
    return value


def update_setting(path, section, setting, value):
    """
    Update a setting
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)


def delete_setting(path, section, setting):
    """
    Delete a setting
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)
        
        
class LoginConfig(object):
    def __new__(cls, conf_path=None, user_type='default'):
        if conf_path is None:
            conf_path = BASE_PATH / 'config.ini'
        instance = object.__new__(cls)
        config = get_config(conf_path)
        section = f'{user_type}_user_conf'
        for option in config.options(section):
            setattr(instance, option, config.get(section, option))
        return instance


if __name__ == "__main__":
    file_path = "../config.ini"
    font = get_setting(file_path, 'Settings', 'font')
    font_size = get_setting(file_path, 'Settings', 'font_size')

    update_setting(file_path, "Settings", "font_size", "12")
    delete_setting(file_path, "Settings", "font_style")