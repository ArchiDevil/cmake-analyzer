import os

from core import parser


def test_parser_can_load_grammar():
    pp = parser.Parser('core/simple_grammar.ebnf')
    assert pp is not None


def test_parser_can_parse_simplest_cmake():
    pp = parser.Parser('core/simple_grammar.ebnf')
    ast = pp.parse_file('tests/parser_tests/sample_cmake.txt')
    assert len(ast) == 1
    command = ast[0]['command']
    assert command['name'] == 'add_library'
    assert len(command['args']) == 3

    args_desc = ['test', 'STATIC', 'main.cpp']
    for i, arg in enumerate(command['args']):
        assert arg['arg'] == [args_desc[i]]


def test_parser_can_parse_space_after_command():
    pp = parser.Parser('core/simple_grammar.ebnf')
    ast = pp.parse_file('tests/parser_tests/space_after_command.txt')
    assert len(ast) == 1
    command = ast[0]['command']
    assert command['name'] == 'add_library'
    assert len(command['args']) == 3

    args_desc = ['main', 'STATIC', 'main.cpp']
    for i, arg in enumerate(command['args']):
        assert arg['arg'] == [args_desc[i]]


def test_parser_can_parse_unquoted_quoted_cmake():
    pp = parser.Parser('core/simple_grammar.ebnf')
    ast = pp.parse_file('tests/parser_tests/unquoted_quoted.txt')
    assert len(ast) == 1
    command = ast[0]['command']
    assert command['name'] == 'add_definitions'
    assert len(command['args']) == 1

    args_desc = ['-DTEST="${SOMETHING}"']
    for i, arg in enumerate(command['args']):
        assert arg['arg'] == [args_desc[i]]


def test_parser_can_save_model():
    pp = parser.Parser('core/simple_grammar.ebnf')
    # .pyc to avoid this file to be commited to the repo
    pp.save_model('model.pyc')
    assert os.path.exists('model.pyc')
