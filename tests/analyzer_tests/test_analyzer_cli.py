import os

from cmake_analyzer import analyzer


def test_analyzer_can_create_parser():
    parser = analyzer.create_parser()
    assert parser is not None


def test_analyzer_can_parse_simplest_case():
    parser = analyzer.create_parser()
    i, e, _, _, _, _, p = analyzer.parse_args(parser, ['-p', 'test'])
    assert p == 'test'
    assert i == ['*']
    assert e == None

    i, e, _, _, _, _, p = analyzer.parse_args(parser, ['--path', 'test_long'])
    assert p == 'test_long'
    assert i == ['*']
    assert e == None


def test_analyzer_can_list_checks():
    parser = analyzer.create_parser()
    _, _, _, l, _, _, _ = analyzer.parse_args(parser, ['--list-checks'])
    assert l == True


def test_analyzer_uses_only_path_or_list():
    parser = analyzer.create_parser()
    flag = False
    try:
        analyzer.parse_args(parser, ['--list-checks',
                                     '-p', 'test'])
    except SystemExit:
        flag = True
    assert flag


def test_analyzer_uses_exclude_dirs():
    parser = analyzer.create_parser()
    i, e, _, _, _, _, _ = analyzer.parse_args(parser,
                                              ['--exclude', 'a', 'b', 'c',
                                               '-p', 'test'])
    assert e == ['a', 'b', 'c']
    assert i == None


def test_analyzer_uses_include_dirs():
    parser = analyzer.create_parser()
    i, e, _, _, _, _, _ = analyzer.parse_args(parser,
                                              ['--include', 'a', 'b', 'c',
                                               '-p', 'test'])
    assert i == ['a', 'b', 'c']
    assert e == None


def test_analyzer_rejects_include_and_exclude_dirs():
    parser = analyzer.create_parser()
    flag = False
    try:
        i, e, _, _, _, _, _ = analyzer.parse_args(parser,
                                                  ['--include', 'a', 'b', 'c',
                                                   '--exclude', 'd', 'e', 'f',
                                                   '-p', 'test'])
    except SystemExit:
        flag = True
    assert flag


def test_analyzer_parses_module_dirs():
    parser = analyzer.create_parser()
    _, _, m, _, _, _, _ = analyzer.parse_args(parser,
                                              ['--custom-checks', 'a',
                                               '-p', 'test'])
    assert m == [os.path.join(os.path.abspath(os.path.curdir), 'cmake_analyzer', 'modules'),
                 'a']


def test_analyzer_parser_checks_list():
    parser = analyzer.create_parser()
    _, _, _, _, c, _, _ = analyzer.parse_args(parser,
                                              ['--checks', 'a', 'b', 'c',
                                               '-p', 'test'])
    assert c == ['a', 'b', 'c']
    
    _, _, _, _, c, _, _ = analyzer.parse_args(parser,
                                              ['-c', 'd', 'e', 'f',
                                               '-p', 'test'])
    assert c == ['d', 'e', 'f']


def test_analyzer_parser_verbose_mode():
    parser = analyzer.create_parser()
    _, _, _, _, _, v, _ = analyzer.parse_args(parser, ['-v',
                                                       '-p', 'test'])
    assert v

    _, _, _, _, _, v, _ = analyzer.parse_args(parser, ['--verbose',
                                                       '-p', 'test'])
    assert v
