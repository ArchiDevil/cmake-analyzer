import os

from cmake_analyzer.core import config_parser

CURRENT_MODULE_PATH = os.path.dirname(__file__)


def test_config_parser_parse_config():
    parser = config_parser.ConfigParser(os.path.join(
        CURRENT_MODULE_PATH, 'correct-config.yaml'))
    assert parser.config
    assert 'module_options' in parser.config.keys()


def test_config_parser_fails_on_inexisting_file():
    flag = False
    try:
        config_parser.ConfigParser('non-existing-dir')
    except FileNotFoundError:
        flag = True
    assert flag


def test_config_parser_fails_on_incorrect_file():
    flag = False
    try:
        config_parser.ConfigParser(os.path.join(
            CURRENT_MODULE_PATH, 'incorrect-config.yaml'))
    except RuntimeError:
        flag = True
    assert flag
