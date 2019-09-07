import os

from cmake_analyzer.modules import style_add_definitions
from cmake_analyzer.core import parser

from tests.modules_tests.generic_module_test_strawman import GenericModuleTestGenerator

CURRENT_MODULE_PATH = os.path.dirname(__file__)

GenericModuleTestGenerator(
    globals(),
    style_add_definitions.AddDefinitionsFinder(),
    os.path.join(CURRENT_MODULE_PATH, 'test_file.txt'),
    [1, 2]
)
