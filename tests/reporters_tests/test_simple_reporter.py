from collections import namedtuple
import builtins

from cmake_analyzer.reporters import simple
from cmake_analyzer.core import reporter_base

Parseinfo = namedtuple('Parseinfo', 'line')


def test_can_create_diagnostic_from_node():
    node = {'parseinfo': Parseinfo(21)}
    file = 'test'
    message = 'error!'
    module = 'test_module'
    simple_diag = reporter_base.create_diagnostic(node, message)
    diag = reporter_base.create_full_diagnostic(simple_diag, file, module)

    assert diag.line == node['parseinfo'].line + 1
    assert diag.file == file
    assert diag.message == message
    assert diag.module == module


def test_simple_reporter_reports_in_console():
    reporter = simple.SimpleReporter()
    line = 21
    node = {'parseinfo': Parseinfo(line)}
    file = 'test'
    message = 'error!'
    module = 'test_module'
    simple_diag = reporter_base.create_diagnostic(node, message)
    diag = reporter_base.create_full_diagnostic(simple_diag, file, module)
    old_print = print

    class Checker(object):
        result = False

        @staticmethod
        def printer(*args):
            Checker.result = True
            assert len(args) == 1
            assert file in args[0]
            assert message in args[0]
            assert str(line + 1) in args[0]
            assert module in args[0]

    builtins.print = Checker.printer
    reporter.report([diag])
    builtins.print = old_print
    assert Checker.result


def test_simple_reporter_ends_without_errors():
    reporter = simple.SimpleReporter()
    reporter.end()
