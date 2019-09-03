import builtins
import os
from collections import namedtuple

from cmake_analyzer.core import parser, traverser, reporter_base

Parseinfo = namedtuple('Parseinfo', 'line')


CURRENT_MODULE_PATH = os.path.dirname(__file__)
GRAMMAR_FILE = 'cmake_analyzer/static/simple_grammar.ebnf'


class SimpleReporter(object):
    def __init__(self):
        self.report_marker = False
        self.end_marker = False

    def report(self, iterable):
        self.report_marker = True

    def end(self):
        self.end_marker = True


class SimpleCheckerFile(object):
    def __init__(self):
        self.checked_modules = []

    def process_file(self, ast, root_directory, filename):
        assert not os.path.isabs(filename)
        self.checked_modules.append(filename)
        return [
            reporter_base.create_full_diagnostic(
                reporter_base.create_diagnostic(
                    {'parseinfo': Parseinfo(0)}, 'test'),
                '/path',
                'module')
        ]


class SimpleCheckerDirectory(object):
    def __init__(self):
        self.checked_dirs = []

    def process_directory(self, root_directory, dirname):
        self.checked_dirs.append(os.path.join(root_directory, dirname))
        return []


class SimpleCheckerEndProcessing(object):
    def __init__(self):
        self.marker = False

    def end_processing(self):
        self.marker = True
        return []


def test_traverser_fails_on_empty_parser():
    try:
        t = traverser.Traverser(None)
    except TypeError:
        return
    assert False


def test_traverser_can_be_initialized():
    p = parser.CMakeParser(GRAMMAR_FILE)
    t = traverser.Traverser(p)
    pass


def test_traverser_can_parse_simple_directory():
    reporter = SimpleReporter()
    p = parser.CMakeParser(GRAMMAR_FILE)
    t = traverser.Traverser(p, reporters=[reporter])
    t.traverse(os.path.join(CURRENT_MODULE_PATH, 'simple_folder'))
    assert reporter.report_marker


def test_traverser_checks_each_correct_file():
    checker = SimpleCheckerFile()
    p = parser.CMakeParser(GRAMMAR_FILE)
    t = traverser.Traverser(p, checkers=[checker])
    t.traverse(os.path.join(CURRENT_MODULE_PATH, 'complex_folder'))
    assert len(checker.checked_modules) == 3


def test_traverser_skips_excluded_files():
    checker = SimpleCheckerFile()
    p = parser.CMakeParser(GRAMMAR_FILE)
    t = traverser.Traverser(
        p, checkers=[checker], exclude_filters=['*subfolder*'])
    t.traverse(os.path.join(CURRENT_MODULE_PATH, 'complex_folder'))
    assert len(checker.checked_modules) == 2


def test_traverser_includes_only_specified_files():
    checker = SimpleCheckerFile()
    p = parser.CMakeParser(GRAMMAR_FILE)
    t = traverser.Traverser(
        p, checkers=[checker], include_filters=['*subfolder*'])
    t.traverse(os.path.join(CURRENT_MODULE_PATH, 'complex_folder'))
    assert len(checker.checked_modules) == 1


def test_traverser_does_not_allow_to_set_includes_and_excludes_simultaneously():
    p = parser.CMakeParser(GRAMMAR_FILE)
    marker = False
    try:
        t = traverser.Traverser(
            p, include_filters=['*'], exclude_filters=['*'])
    except ValueError:
        marker = True
    assert marker


def test_traverser_raises_error_on_wrong_root_dir():
    p = parser.CMakeParser(GRAMMAR_FILE)
    t = traverser.Traverser(p)
    try:
        t.traverse(os.path.join(CURRENT_MODULE_PATH, 'incorrect_folder'))
    except RuntimeError:
        return
    assert False


def test_traverser_tells_reporters_end_on_end_processing():
    reporter = SimpleReporter()
    p = parser.CMakeParser(GRAMMAR_FILE)
    t = traverser.Traverser(p, reporters=[reporter])
    t.traverse(os.path.join(CURRENT_MODULE_PATH, 'simple_folder'))
    assert reporter.end_marker


def test_traverser_print_files_in_verbose_mode():
    class Checker(object):
        invocations = 0

        @staticmethod
        def checker(*args):
            Checker.invocations += 1
            assert os.path.exists(args[0].split()[-1])

    p = parser.CMakeParser(GRAMMAR_FILE)
    t = traverser.Traverser(p, verbose=True)
    old_print = builtins.print
    builtins.print = Checker.checker
    t.traverse(os.path.join(CURRENT_MODULE_PATH, 'simple_folder'))
    assert Checker.invocations == 1
    builtins.print = old_print


def test_traverser_correctly_process_dirs():
    checker = SimpleCheckerDirectory()
    p = parser.CMakeParser(GRAMMAR_FILE)
    t = traverser.Traverser(p, checkers=[checker])
    t.traverse(os.path.join(CURRENT_MODULE_PATH, 'complex_folder'))
    assert len(checker.checked_dirs) == 3


def test_traverser_correctly_ends():
    checker = SimpleCheckerEndProcessing()
    p = parser.CMakeParser(GRAMMAR_FILE)
    t = traverser.Traverser(p, checkers=[checker])
    t.traverse(os.path.join(CURRENT_MODULE_PATH, 'complex_folder'))
    assert checker.marker


def test_traverser_works_with_many_checkers():
    checkers = [SimpleCheckerFile(), SimpleCheckerDirectory(),
                SimpleCheckerEndProcessing()]
    p = parser.CMakeParser(GRAMMAR_FILE)
    t = traverser.Traverser(p, checkers=checkers)
    t.traverse(os.path.join(CURRENT_MODULE_PATH, 'complex_folder'))
    assert len(checkers[0].checked_modules) == 3
    assert len(checkers[1].checked_dirs) == 3
    assert checkers[2].marker
