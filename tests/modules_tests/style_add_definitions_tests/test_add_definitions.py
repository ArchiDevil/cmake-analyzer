import os

from cmake_analyzer.modules import style_add_definitions
from cmake_analyzer.core import parser

CURRENT_MODULE_PATH = os.path.dirname(__file__)


def test_add_definitions_is_found():
    p = parser.CMakeParser('cmake_analyzer/static/simple_grammar.ebnf')
    c = style_add_definitions.AddDefinitionsFinder()
    diags = c.process_file(p.parse_file(os.path.join(CURRENT_MODULE_PATH, 'test_file.txt')),
                           '/some/directory/',
                           'CMakeLists.txt')
    assert len(diags) == 2
