import os
from core import parser, traverser

CURRENT_MODULE_PATH = os.path.dirname(__file__)

class SimpleReporter(object):
    def __init__(self):
        self.report_marker = False
        self.end_marker = False

    def report(self, iterable):
        self.report_marker = True

    def end(self):
        self.end_marker = True


class SimpleChecker(object):
    def __init__(self):
        self.checked_modules = []

    def process(self, ast, root_directory, filename):
        assert not os.path.isabs(filename)
        self.checked_modules.append(filename)
        return []


def test_traverser_fails_on_empty_parser():
    try:
        t = traverser.Traverser(None)
    except TypeError:
        return
    assert False


def test_traverser_can_be_initialized():
    p = parser.CMakeParser('core/simple_grammar.ebnf')
    t = traverser.Traverser(p)
    pass


def test_traverser_can_parse_simple_directory():
    reporter = SimpleReporter()
    p = parser.CMakeParser('core/simple_grammar.ebnf')
    t = traverser.Traverser(p, reporters=[reporter])
    t.traverse(os.path.join(CURRENT_MODULE_PATH, 'simple_folder'))
    assert reporter.report_marker


def test_traverser_checks_each_correct_file():
    checker = SimpleChecker()
    p = parser.CMakeParser('core/simple_grammar.ebnf')
    t = traverser.Traverser(p, checkers=[checker])
    t.traverse(os.path.join(CURRENT_MODULE_PATH, 'complex_folder'))
    assert len(checker.checked_modules) == 3


def test_traverser_raises_error_on_wrong_root_dir():
    p = parser.CMakeParser('core/simple_grammar.ebnf')
    t = traverser.Traverser(p)
    try:
        t.traverse(os.path.join(CURRENT_MODULE_PATH, 'incorrect_folder'))
    except RuntimeError:
        return
    assert False


def test_traverser_tells_reporters_end_on_end_processing():
    reporter = SimpleReporter()
    p = parser.CMakeParser('core/simple_grammar.ebnf')
    t = traverser.Traverser(p, reporters=[reporter])
    t.traverse(os.path.join(CURRENT_MODULE_PATH, 'simple_folder'))
    assert reporter.end_marker
