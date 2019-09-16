from typing import Dict

import yaml


class ConfigParser:
    def __init__(self, config_file_path):
        with open(config_file_path) as config_stream:
            self.__cfg = yaml.safe_load(config_stream)

        if not self.__check_config():
            raise RuntimeError("Incorrect config syntax")

    def __check_config(self) -> bool:
        if not 'module_options' in self.config.keys():
            return False
        return True

    @property
    def config(self) -> Dict[str, Dict]:
        return self.__cfg
