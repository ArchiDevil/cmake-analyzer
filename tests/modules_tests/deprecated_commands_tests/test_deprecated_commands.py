import os

from cmake_analyzer.core import parser
from cmake_analyzer.modules import deprecated_commands

from tests.modules_tests.generic_module_test_strawman import GenericModuleTestGenerator

CURRENT_MODULE_PATH = os.path.dirname(__file__)

GenericModuleTestGenerator(
    globals(),
    deprecated_commands.DeprecatedCommandsChecker(),
    os.path.join(CURRENT_MODULE_PATH, 'deprecated_commands_test.txt'),
    [x + 1 for x in range(18)]
)
