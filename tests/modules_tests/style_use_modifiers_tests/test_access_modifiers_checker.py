import os

from cmake_analyzer.modules import style_use_access_modifiers
from cmake_analyzer.core import parser

CURRENT_MODULE_PATH = os.path.dirname(__file__)


def test_found_wrong_commands():
    p = parser.CMakeParser('cmake_analyzer/static/simple_grammar.ebnf')
    c = style_use_access_modifiers.AccessModifiersChecker()
    diags = c.process_file(p.parse_file(os.path.join(CURRENT_MODULE_PATH, 'test_file.txt')),
                           '/some/directory/',
                           'CMakeLists.txt')
    assert len(diags) == 2
    lines = [11, 14]
    for i, diag in enumerate(diags):
        assert lines[i] == diag.line
