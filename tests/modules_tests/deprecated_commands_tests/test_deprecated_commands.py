import os

from cmake_analyzer.core import parser
from cmake_analyzer.modules import deprecated_commands

CURRENT_MODULE_PATH = os.path.dirname(__file__)


def test_deprecated_commands_checker_finds_deprecated_command():
    p = parser.CMakeParser('cmake_analyzer/static/simple_grammar.ebnf')
    c = deprecated_commands.DeprecatedCommandsChecker()
    file_to_check = 'deprecated_commands_test.txt'
    ast = p.parse_file(os.path.join(CURRENT_MODULE_PATH, file_to_check))
    diags = c.process_file(ast, CURRENT_MODULE_PATH, file_to_check)
    assert isinstance(diags, list)
    assert len(diags) == 18
    lines = [x + 1 for x in range(18)]
    for i, diag in enumerate(diags):
        assert lines[i] == diag.line
