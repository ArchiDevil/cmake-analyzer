import os

from cmake_analyzer import analyzer


def test_analyzer_can_create_parser():
    parser = analyzer.create_parser()
    assert parser is not None


def test_analyzer_can_parse_simplest_case():
    parser = analyzer.create_parser()
    parsed_args = analyzer.parse_args(parser, ['-p', 'test'])
    assert parsed_args.check_path == 'test'
    assert parsed_args.include_filters == ['*']
    assert parsed_args.exclude_filters is None

    parsed_args = analyzer.parse_args(parser, ['--path', 'test_long'])
    assert parsed_args.check_path == 'test_long'
    assert parsed_args.include_filters == ['*']
    assert parsed_args.exclude_filters is None


def test_analyzer_can_list_checks():
    parser = analyzer.create_parser()
    parsed_args = analyzer.parse_args(parser, ['--list-checks'])
    assert parsed_args.do_list_checks is True


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
    parsed_args = analyzer.parse_args(parser,
                                      ['--exclude', 'a', 'b', 'c',
                                       '-p', 'test'])
    assert parsed_args.exclude_filters == ['a', 'b', 'c']
    assert parsed_args.include_filters is None


def test_analyzer_uses_include_dirs():
    parser = analyzer.create_parser()
    parsed_args = analyzer.parse_args(parser,
                                      ['--include', 'a', 'b', 'c',
                                       '-p', 'test'])
    assert parsed_args.include_filters == ['a', 'b', 'c']
    assert parsed_args.exclude_filters is None


def test_analyzer_rejects_include_and_exclude_dirs():
    parser = analyzer.create_parser()
    flag = False
    try:
        analyzer.parse_args(parser,
                            ['--include', 'a', 'b', 'c',
                             '--exclude', 'd', 'e', 'f',
                             '-p', 'test'])
    except SystemExit:
        flag = True
    assert flag


def test_analyzer_parses_module_dirs():
    parser = analyzer.create_parser()
    parsed_args = analyzer.parse_args(parser,
                                      ['--custom-checks', 'a',
                                       '-p', 'test'])
    assert parsed_args.modules_list == [os.path.join(os.path.abspath(os.path.curdir),
                                                     'cmake_analyzer',
                                                     'modules'),
                                        'a']


def test_analyzer_parser_checks_list():
    parser = analyzer.create_parser()
    parsed_args = analyzer.parse_args(parser,
                                      ['--checks', 'a', 'b', 'c',
                                       '-p', 'test'])
    assert parsed_args.checks == ['a', 'b', 'c']

    parsed_args = analyzer.parse_args(parser,
                                      ['-c', 'd', 'e', 'f',
                                       '-p', 'test'])
    assert parsed_args.checks == ['d', 'e', 'f']


def test_analyzer_parser_verbose_mode():
    parser = analyzer.create_parser()
    parsed_args = analyzer.parse_args(parser, ['-v',
                                               '-p', 'test'])
    assert parsed_args.verbose

    parsed_args = analyzer.parse_args(parser, ['--verbose',
                                               '-p', 'test'])
    assert parsed_args.verbose


def test_analyzer_parser_can_parse_config():
    parser = analyzer.create_parser()
    path = 'some/path/to/config'
    parsed_args = analyzer.parse_args(parser, ['--config', path,
                                               '-p', 'test'])
    assert parsed_args.config_path == path
