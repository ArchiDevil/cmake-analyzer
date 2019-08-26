import os

from core import modules_loader

CURRENT_MODULE_PATH = os.path.dirname(__file__)
TEST_MODULES_PATH = os.path.join(CURRENT_MODULE_PATH, 'test_modules')


def test_modules_loader_can_load_some_module():
    loader = modules_loader.ModulesLoader(TEST_MODULES_PATH)
    modules = loader.loaded_modules
    assert len(modules) == 1
    for module in modules:
        assert module is not None


def test_modules_loader_can_load_some_checker():
    loader = modules_loader.ModulesLoader(TEST_MODULES_PATH)
    checkers = loader.loaded_checkers
    assert len(checkers)


def test_modules_loader_loads_only_valid_checkers():
    loader = modules_loader.ModulesLoader(TEST_MODULES_PATH)
    checkers = loader.loaded_checkers
    assert len(checkers) == 2
    for checker in checkers:
        try:
            checker.process({}, '', '')
        except NotImplementedError:
            # one of the test classes is not implemented intentionally
            pass
