import os

from cmake_analyzer.core import parser

CURRENT_MODULE_PATH = os.path.dirname(__file__)
GRAMMAR_FILE = 'cmake_analyzer/static/simple_grammar.ebnf'


def test_parser_can_load_grammar():
    pp = parser.CMakeParser(GRAMMAR_FILE)
    assert pp is not None


def test_parser_can_parse_simplest_cmake():
    pp = parser.CMakeParser(GRAMMAR_FILE)
    ast = pp.parse_file(os.path.join(CURRENT_MODULE_PATH, 'sample_cmake.txt'))
    assert len(ast) == 1
    command = ast[0]
    assert command['name'] == 'add_library'
    assert len(command['args']) == 3

    args_desc = ['test', 'STATIC', 'main.cpp']
    for i, arg in enumerate(command['args']):
        assert arg['arg'] == args_desc[i]


def test_parser_can_parse_space_after_command():
    pp = parser.CMakeParser(GRAMMAR_FILE)
    ast = pp.parse_file(os.path.join(CURRENT_MODULE_PATH, 'space_after_command.txt'))
    assert len(ast) == 1
    command = ast[0]
    assert command['name'] == 'add_library'
    assert len(command['args']) == 3

    args_desc = ['main', 'STATIC', 'main.cpp']
    for i, arg in enumerate(command['args']):
        assert arg['arg'] == args_desc[i]


def test_parser_can_parse_unquoted_quoted_cmake():
    pp = parser.CMakeParser(GRAMMAR_FILE)
    ast = pp.parse_file(os.path.join(CURRENT_MODULE_PATH, 'unquoted_quoted.txt'))
    assert len(ast) == 1
    command = ast[0]
    assert command['name'] == 'add_definitions'
    assert len(command['args']) == 1

    args_desc = ['-DTEST="${SOMETHING}"']
    for i, arg in enumerate(command['args']):
        assert arg['arg'] == args_desc[i]


def test_parser_can_save_model():
    pp = parser.CMakeParser(GRAMMAR_FILE)
    # .pyc to avoid this file to be commited to the repo
    pp.save_model(os.path.join(CURRENT_MODULE_PATH, 'model.pyc'))
    assert os.path.exists(os.path.join(CURRENT_MODULE_PATH, 'model.pyc'))


def test_parser_handles_corner_cases():
    pp = parser.CMakeParser(GRAMMAR_FILE)
    ast = pp.parse_file(os.path.join(CURRENT_MODULE_PATH, 'corner_case1.txt'))
    assert len(ast) == 3
