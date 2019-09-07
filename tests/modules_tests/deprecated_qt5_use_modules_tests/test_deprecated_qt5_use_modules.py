import os

from cmake_analyzer.core import parser
from cmake_analyzer.modules import deprecated_qt5_use_modules

from tests.modules_tests.generic_module_test_strawman import GenericModuleTestGenerator

CURRENT_MODULE_PATH = os.path.dirname(__file__)

GenericModuleTestGenerator(
    globals(),
    deprecated_qt5_use_modules.DeprecatedQt5UseModulesChecker(),
    os.path.join(CURRENT_MODULE_PATH, 'qt5_use_modules_test.txt'),
    [1, 3]
)
