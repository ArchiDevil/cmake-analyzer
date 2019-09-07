import os

from cmake_analyzer.core import parser
from cmake_analyzer.modules import deprecated_link_prefix

from tests.modules_tests.generic_module_test_strawman import GenericModuleTestGenerator

CURRENT_MODULE_PATH = os.path.dirname(__file__)

GenericModuleTestGenerator(
    globals(),
    deprecated_link_prefix.DeprecatedLinkPrefixChecker(),
    os.path.join(CURRENT_MODULE_PATH, 'link_prefix_test.txt'),
    [1, 6, 16]
)
