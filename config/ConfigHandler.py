import ConfigParser
import os


class ConfigHandler:
    _cfg = ConfigParser.ConfigParser()
    _cfg.read(os.path.join(os.path.dirname(__file__), 'config.cfg'))

    _home_dir = os.path.expanduser('~')

    CONFIG_MODE = None

    @staticmethod
    def set_config_mode(config_mode):
        ConfigHandler.CONFIG_MODE = config_mode

    @staticmethod
    def get_config_mode():
        return ConfigHandler.CONFIG_MODE

    @staticmethod
    def get(key, config_mode=None):
        if not config_mode:
            value = ConfigHandler._cfg.get(ConfigHandler.CONFIG_MODE, key)
        else:
            value = ConfigHandler._cfg.get(config_mode, key)

        # this takes care of adding the proper home path of the present user to the filepaths
        if value[:2] == "~/":
            value = os.path.join(ConfigHandler._home_dir, value[2:])

        return value

    @staticmethod
    def getint(key, config_mode):
        return ConfigHandler._cfg.getint(config_mode, key)

    @staticmethod
    def getfloat(key, config_mode):
        return ConfigHandler._cfg.getfloat(config_mode, key)

    @staticmethod
    def get_boolean(key, config_mode):
        return ConfigHandler._cfg.getboolean(config_mode, key)
