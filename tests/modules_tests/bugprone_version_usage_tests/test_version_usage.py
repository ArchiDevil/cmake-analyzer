import os

from cmake_analyzer.modules import bugprone_version_usage
from cmake_analyzer.core import parser

from tests.modules_tests.generic_module_test_strawman import GenericModuleTestGenerator

CURRENT_MODULE_PATH = os.path.dirname(__file__)

GenericModuleTestGenerator(
    globals(),
    bugprone_version_usage.VersionUsageChecker(),
    os.path.join(CURRENT_MODULE_PATH, 'test_file.txt'),
    []
)


def test_project_usage_finds_errors_in_underlying():
    p = parser.CMakeParser('cmake_analyzer/static/simple_grammar.ebnf')
    c = bugprone_version_usage.VersionUsageChecker()
    diags = c.process_file(p.parse_file(os.path.join(CURRENT_MODULE_PATH, 'test_file.txt')),
                           '/some/directory/',
                           'inner/CMakeLists.txt')
    assert len(diags) == 2
    lines = [1, 3]
    for i, diag in enumerate(diags):
        assert lines[i] == diag.line
