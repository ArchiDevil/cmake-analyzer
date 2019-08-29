import os

from core import modules_loader

CURRENT_MODULE_PATH = os.path.dirname(__file__)
TEST_MODULES_PATH = os.path.join(CURRENT_MODULE_PATH, 'test_modules')


def test_modules_loader_can_load_some_modules():
    loader = modules_loader.ModulesLoader([TEST_MODULES_PATH])
    modules = loader.loaded_modules
    assert len(modules) == 2
    for module in modules:
        assert module is not None


def test_modules_loader_applies_filter_to_modules():
    loader = modules_loader.ModulesLoader([TEST_MODULES_PATH], ['test*'])
    modules = loader.loaded_modules
    assert len(modules) == 1
    for module in modules:
        assert module is not None


def test_modules_loader_can_load_some_checker():
    loader = modules_loader.ModulesLoader([TEST_MODULES_PATH])
    checkers = loader.loaded_checkers
    assert len(checkers)


def test_modules_loader_loads_only_valid_checkers():
    loader = modules_loader.ModulesLoader([TEST_MODULES_PATH])
    checkers = loader.loaded_checkers
    assert len(checkers) == 3


def test_modules_loader_can_load_user_modules():
    loader = modules_loader.ModulesLoader([TEST_MODULES_PATH, os.path.join(CURRENT_MODULE_PATH, 'custom_modules')])
    checkers = loader.loaded_checkers
    assert len(checkers) == 4
