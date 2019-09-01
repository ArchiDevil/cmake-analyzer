import os

from modules import bugprone_version_usage
from core import parser

CURRENT_MODULE_PATH = os.path.dirname(__file__)


def test_project_usage_skips_root():
    p = parser.CMakeParser('core/simple_grammar.ebnf')
    c = bugprone_version_usage.VersionUsageChecker()
    diags = c.process_file(p.parse_file(os.path.join(CURRENT_MODULE_PATH, 'test_file.txt')),
                           '/some/directory/',
                           'CMakeLists.txt')
    assert len(diags) == 0


def test_project_usage_finds_errors_in_underlying():
    p = parser.CMakeParser('core/simple_grammar.ebnf')
    c = bugprone_version_usage.VersionUsageChecker()
    diags = c.process_file(p.parse_file(os.path.join(CURRENT_MODULE_PATH, 'test_file.txt')),
                           '/some/directory/',
                           'inner/CMakeLists.txt')
    assert len(diags) == 2
