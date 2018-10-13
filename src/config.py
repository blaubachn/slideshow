from configparser import ConfigParser
from os.path import isfile, expanduser

class Configuration_Manager:
    def __init__(self, config_file):
        self.config_file = config_file
        if not isfile(self.config_file):
            self.set_config_defaults()

    def get_config(self):
        config = ConfigParser()
        config.read(self.config_file)
        return {
            'directory': config.get('configuration', 'directory'),
            'install': config.get('configuration', 'install')
        }

    def set_config(self, directory, install):
        new_config = ConfigParser()
        new_config.add_section('configuration')
        new_config.set('configuration', 'directory', directory)
        new_config.set('configuration', 'install', install)
        with open(self.config_file, 'w') as configfile:
            new_config.write(configfile)

    def set_config_defaults(self):
        self.set_config(expanduser("~"), 'standard/snap')